import os

class ScriptFiles:
    def __init__(self, scripts_directory: str):
        self.scripts_directory = scripts_directory

    def list_script_files(self) -> list[str]:
        files = []
        for file in os.listdir(self.scripts_directory):
            if file.endswith('.sql'):
                files.append(file)
        return files

    def read_script_file(self, script_name: str) -> str:
        try:
            with open(f"{os.getenv('query_filepath')}/{script_name}", "r") as q:
                query = ""
                for line in q:
                    query += line
        except FileNotFoundError:
            raise FileNotFoundError(f"Query File:\n{script_name}\nnot found")
        return query
    
    