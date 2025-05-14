import http.server
import socketserver
import urllib.parse
from app.predict import predict_phishing, predict_phishing_proba
from app.language_detection import detect_language

PORT = 8080
HTML_FORM = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Phishing & Language Detection</title>
    <style>body { font-family: Arial; margin: 40px; } textarea, input[type=text] { width: 100%; }</style>
</head>
<body>
    <h1>Phishing & Language Detection</h1>
    <form method="POST">
        <label for="text">Message:</label><br>
        <textarea name="text" rows="4" required></textarea><br><br>
        <label for="url">URL (optional):</label><br>
        <input type="text" name="url"><br><br>
        <button type="submit">Check</button>
    </form>
    {result}
</body>
</html>
'''

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(HTML_FORM.format(result='').encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        fields = urllib.parse.parse_qs(post_data.decode())
        text = fields.get('text', [''])[0]
        url = fields.get('url', [''])[0]
        if text:
            lang = detect_language(text)
            pred = predict_phishing(text, url)
            proba = predict_phishing_proba(text, url)
            label = 'Phishing' if pred == 1 else ('Legitimate' if pred == 0 else 'Unknown')
            result_html = f'<h2>Prediction: <span style="color:{'red' if pred == 1 else 'green' if pred == 0 else 'gray'}">{label}</span></h2>'
            result_html += f'<h3>Language: <span style="color:#31708f">{lang}</span></h3>'
            result_html += f'<h3>Phishing Probability: <span style="color:#b85c00">{proba:.2%}</span></h3>'
        else:
            result_html = '<h3 style="color:red">Please enter a message.</h3>'
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(HTML_FORM.format(result=result_html).encode())

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()