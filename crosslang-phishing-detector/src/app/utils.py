def log_message(message):
    with open("app.log", "a") as log_file:
        log_file.write(message + "\n")

def load_config(config_file):
    import json
    with open(config_file, "r") as file:
        return json.load(file)

def save_model(model, filename):
    import joblib
    joblib.dump(model, filename)

def load_model(filename):
    import joblib
    return joblib.load(filename)