# #!/bin/bash

# # Create directories
# mkdir -p backend frontend db static

# # Create backend files
# echo "from flask import Flask, request, jsonify
# from database import init_db, add_dataset_entry, get_all_datasets, export_dataset

# app = Flask(__name__)
# db_path = \"db/synthetic_data.db\"

# # Initialize the database
# init_db(db_path)

# @app.route('/api/datasets', methods=['GET'])
# def fetch_datasets():
#     datasets = get_all_datasets(db_path)
#     return jsonify(datasets)

# @app.route('/api/datasets', methods=['POST'])
# def add_dataset():
#     data = request.json
#     if not data or 'prompt' not in data or 'completion' not in data or 'system_prompt' not in data:
#         return jsonify({'error': 'Invalid payload'}), 400
#     add_dataset_entry(db_path, data['prompt'], data['completion'], data['system_prompt'])
#     return jsonify({'message': 'Dataset entry added successfully'})

# @app.route('/api/export', methods=['GET'])
# def export():
#     format = request.args.get('format', 'csv')
#     exported_file = export_dataset(db_path, format)
#     return jsonify({'message': f'Dataset exported to {exported_file}'}), 200

# if __name__ == '__main__':
#     app.run(debug=True)" > backend/app.py

# echo "import sqlite3
# import pandas as pd

# def init_db(db_path):
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS datasets (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             prompt TEXT NOT NULL,
#             completion TEXT NOT NULL,
#             system_prompt TEXT NOT NULL
#         )
#     ''')
#     conn.commit()
#     conn.close()

# def add_dataset_entry(db_path, prompt, completion, system_prompt):
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#     cursor.execute('INSERT INTO datasets (prompt, completion, system_prompt) VALUES (?, ?, ?)',
#                    (prompt, completion, system_prompt))
#     conn.commit()
#     conn.close()

# def get_all_datasets(db_path):
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM datasets')
#     rows = cursor.fetchall()
#     conn.close()
#     return [{'id': row[0], 'prompt': row[1], 'completion': row[2], 'system_prompt': row[3]} for row in rows]

# def export_dataset(db_path, format):
#     conn = sqlite3.connect(db_path)
#     df = pd.read_sql_query('SELECT * FROM datasets', conn)
#     if format == 'csv':
#         file_name = 'synthetic_data.csv'
#         df.to_csv(file_name, index=False)
#     elif format == 'jsonl':
#         file_name = 'synthetic_data.jsonl'
#         df.to_json(file_name, orient='records', lines=True)
#     conn.close()
#     return file_name" > backend/database.py

# echo "Flask
# pandas
# sqlite3" > backend/requirements.txt

# # Create frontend files
# echo "import gradio as gr
# import requests

# API_URL = \"http://127.0.0.1:5000/api\"

# def create_dataset_entry(prompt, completion, system_prompt):
#     data = {\"prompt\": prompt, \"completion\": completion, \"system_prompt\": system_prompt}
#     response = requests.post(f\"{API_URL}/datasets\", json=data)
#     return response.json()

# def fetch_dataset():
#     response = requests.get(f\"{API_URL}/datasets\")
#     return response.json()

# def export_dataset(format):
#     response = requests.get(f\"{API_URL}/export\", params={\"format\": format})
#     return response.json()['message']

# def gradio_ui():
#     with gr.Blocks() as app:
#         gr.Markdown(\"### Dataset Creation Tool\")
        
#         with gr.Row():
#             prompt = gr.Textbox(label=\"Prompt\", placeholder=\"Enter a sample prompt\")
#             completion = gr.Textbox(label=\"Completion\", placeholder=\"Enter a sample completion\")
#             system_prompt = gr.Textbox(label=\"System Prompt\", placeholder=\"Enter the system prompt\")
        
#         save_button = gr.Button(\"Add to Dataset\")
#         save_output = gr.Textbox(label=\"Save Status\")

#         save_button.click(create_dataset_entry, 
#                           inputs=[prompt, completion, system_prompt], 
#                           outputs=[save_output])

#         # Dataset Fetch Section
#         fetch_button = gr.Button(\"Fetch All Datasets\")
#         dataset_output = gr.DataFrame()

#         fetch_button.click(fetch_dataset, outputs=[dataset_output])

#         # Export Section
#         export_format = gr.Radio([\"csv\", \"jsonl\"], label=\"Export Format\")
#         export_button = gr.Button(\"Export Dataset\")
#         export_output = gr.Textbox(label=\"Export Status\")

#         export_button.click(export_dataset, inputs=[export_format], outputs=[export_output])

#     return app

# if __name__ == \"__main__\":
#     ui = gradio_ui()
#     ui.launch()" > frontend/interface.py

# echo "gradio
# requests" > frontend/requirements.txt

# # Create static files
# echo "/* Optional custom styles for Gradio */" > static/style.css

# # Create README file
# echo "# Synthetic Data Project

# ## Backend
# To run the backend, navigate to the 'backend' folder and install the dependencies:

# \```bash
# pip install -r requirements.txt
# python app.py
# \```

# ## Frontend
# To run the frontend, navigate to the 'frontend' folder and install the dependencies:

# \```bash
# pip install -r requirements.txt
# python interface.py
# \```

# ## Database
# The SQLite database is auto-created in the 'db' folder when you run the backend for the first time.

# ## Running Together
# Use the provided 'run.sh' script to start both backend and frontend." > README.md

# # Create run.sh script
# echo "#!/bin/bash

# # Start Flask Backend
# echo \"Starting backend...\"
# cd backend && python app.py &

# # Start Gradio Frontend
# echo \"Starting frontend...\"
# cd ../frontend && python interface.py" > run.sh

# # Make run.sh executable
# chmod +x run.sh

# # Final message
# echo "Project files and structure have been created successfully."


#!/bin/bash

# Create main project directories
mkdir -p app tests

# Create empty files in the app directory
touch app/__init__.py
touch app/routes.py
touch app/generator.py
touch app/deduplicator.py
touch app/config.py
touch app/utils.py

# Create empty files in the tests directory
touch tests/test_routes.py
touch tests/test_generator.py
touch tests/test_deduplicator.py
touch tests/test_utils.py

# Create root-level files
touch requirements.txt
touch run.py
touch .env

# Print success message
echo "Project structure created successfully!"
