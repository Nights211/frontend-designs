#!/usr/bin/env python3
import os
import sys
import webbrowser
import subprocess
import time
from pathlib import Path

BASE_DIR = Path(__file__).parent

def find_examples():
    """Find all examples in the repo"""
    examples = {
        'html': [],
        'typescript': [],
        'gradio': [],
        'streamlit': []
    }
    
    # HTML examples
    html_dir = BASE_DIR / 'html-css-js'
    if html_dir.exists():
        examples['html'] = [d.name for d in html_dir.iterdir() if d.is_dir()]
    
    # TypeScript examples
    ts_dir = BASE_DIR / 'typescript-designs'
    if ts_dir.exists():
        examples['typescript'] = [d.name for d in ts_dir.iterdir() if d.is_dir()]
    
    # Python frontends
    py_dir = BASE_DIR / 'python-frontends'
    if py_dir.exists():
        for d in py_dir.iterdir():
            if d.is_dir():
                if (d / 'app.py').exists():
                    with open(d / 'app.py') as f:
                        content = f.read()
                        if 'gradio' in content:
                            examples['gradio'].append(d.name)
                        elif 'streamlit' in content:
                            examples['streamlit'].append(d.name)
    
    return examples

def list_examples():
    """List all available examples"""
    examples = find_examples()
    
    print("\n📦 Available Examples:\n")
    
    if examples['html']:
        print("HTML/CSS/JS:")
        for ex in examples['html']:
            print(f"  • {ex}")
    
    if examples['typescript']:
        print("\nTypeScript:")
        for ex in examples['typescript']:
            print(f"  • {ex}")
    
    if examples['gradio']:
        print("\nGradio:")
        for ex in examples['gradio']:
            print(f"  • {ex}")
    
    if examples['streamlit']:
        print("\nStreamlit:")
        for ex in examples['streamlit']:
            print(f"  • {ex}")
    
    print("\n💡 Usage:")
    print("  ./launch.py html <example-name>")
    print("  ./launch.py gradio <example-name>")
    print("  ./launch.py streamlit <example-name>")
    print("  ./launch.py backend")

def launch_html(example_name):
    """Launch HTML example"""
    example_path = BASE_DIR / 'html-css-js' / example_name
    
    if not example_path.exists():
        print(f"❌ Example '{example_name}' not found")
        return
    
    print(f"🚀 Launching {example_name}...")
    print("📡 Starting server on http://localhost:8000")
    print("Press Ctrl+C to stop\n")
    
    time.sleep(1)
    webbrowser.open('http://localhost:8000')
    
    os.chdir(example_path)
    subprocess.run(['python3', '-m', 'http.server', '8000'])

def launch_gradio(example_name):
    """Launch Gradio app"""
    example_path = BASE_DIR / 'python-frontends' / example_name
    app_file = example_path / 'app.py'
    
    if not app_file.exists():
        print(f"❌ Example '{example_name}' not found")
        return
    
    print(f"🚀 Launching {example_name}...")
    os.chdir(example_path)
    subprocess.run(['python3', 'app.py'])

def launch_streamlit(example_name):
    """Launch Streamlit app"""
    example_path = BASE_DIR / 'python-frontends' / example_name
    app_file = example_path / 'app.py'
    
    if not app_file.exists():
        print(f"❌ Example '{example_name}' not found")
        return
    
    print(f"🚀 Launching {example_name}...")
    os.chdir(example_path)
    subprocess.run(['streamlit', 'run', 'app.py'])

def launch_backend():
    """Launch FastAPI backend"""
    backend_path = BASE_DIR / 'backend'
    main_file = backend_path / 'main.py'
    
    if not main_file.exists():
        print("❌ Backend not set up yet (backend/main.py not found)")
        return
    
    print("🚀 Launching FastAPI backend...")
    print("📡 API will be available at http://localhost:8000")
    print("📚 Docs at http://localhost:8000/docs")
    print("Press Ctrl+C to stop\n")
    
    os.chdir(backend_path)
    subprocess.run(['uvicorn', 'main:app', '--reload'])

def main():
    if len(sys.argv) < 2:
        list_examples()
        return
    
    command = sys.argv[1]
    
    if command == 'list':
        list_examples()
    elif command == 'html' and len(sys.argv) > 2:
        launch_html(sys.argv[2])
    elif command == 'gradio' and len(sys.argv) > 2:
        launch_gradio(sys.argv[2])
    elif command == 'streamlit' and len(sys.argv) > 2:
        launch_streamlit(sys.argv[2])
    elif command == 'backend':
        launch_backend()
    else:
        print("❌ Invalid command")
        list_examples()

if __name__ == '__main__':
    main()
