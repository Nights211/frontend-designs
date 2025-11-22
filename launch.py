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
    
    print(f"\n🚀 Launching {example_name}...")
    print("📡 Starting server on http://localhost:8000")
    print("Press Ctrl+C to stop and return to menu\n")
    
    time.sleep(1)
    webbrowser.open('http://localhost:8000')
    
    os.chdir(example_path)
    try:
        subprocess.run(['python3', '-m', 'http.server', '8000'])
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped")

def launch_gradio(example_name):
    """Launch Gradio app"""
    example_path = BASE_DIR / 'python-frontends' / example_name
    app_file = example_path / 'app.py'
    
    if not app_file.exists():
        print(f"❌ Example '{example_name}' not found")
        return
    
    print(f"\n🚀 Launching {example_name}...")
    print("Press Ctrl+C to stop and return to menu\n")
    os.chdir(example_path)
    try:
        subprocess.run(['python3', 'app.py'])
    except KeyboardInterrupt:
        print("\n\n✅ App stopped")

def launch_streamlit(example_name):
    """Launch Streamlit app"""
    example_path = BASE_DIR / 'python-frontends' / example_name
    app_file = example_path / 'app.py'
    
    if not app_file.exists():
        print(f"❌ Example '{example_name}' not found")
        return
    
    print(f"\n🚀 Launching {example_name}...")
    print("Press Ctrl+C to stop and return to menu\n")
    os.chdir(example_path)
    try:
        subprocess.run(['streamlit', 'run', 'app.py'])
    except KeyboardInterrupt:
        print("\n\n✅ App stopped")

def launch_backend():
    """Launch FastAPI backend"""
    backend_path = BASE_DIR / 'backend'
    main_file = backend_path / 'main.py'
    
    if not main_file.exists():
        print("❌ Backend not set up yet (backend/main.py not found)")
        return
    
    print("\n🚀 Launching FastAPI backend...")
    print("📡 API will be available at http://localhost:8000")
    print("📚 Docs at http://localhost:8000/docs")
    print("Press Ctrl+C to stop and return to menu\n")
    
    os.chdir(backend_path)
    try:
        subprocess.run(['uvicorn', 'main:app', '--reload'])
    except KeyboardInterrupt:
        print("\n\n✅ Backend stopped")

def interactive_menu():
    """Interactive menu for selecting examples"""
    while True:
        examples = find_examples()
        
        # Build menu options
        options = []
        if examples['html']:
            for ex in examples['html']:
                options.append(('html', ex))
        if examples['typescript']:
            for ex in examples['typescript']:
                options.append(('typescript', ex))
        if examples['gradio']:
            for ex in examples['gradio']:
                options.append(('gradio', ex))
        if examples['streamlit']:
            for ex in examples['streamlit']:
                options.append(('streamlit', ex))
        
        # Check if backend exists
        backend_exists = (BASE_DIR / 'backend' / 'main.py').exists()
        
        if not options and not backend_exists:
            print("❌ No examples found")
            return
        
        print("\n🚀 Frontend Designs Launcher\n")
        
        # Display menu
        idx = 1
        for typ, name in options:
            print(f"  {idx}. [{typ.upper()}] {name}")
            idx += 1
        
        if backend_exists:
            print(f"  {idx}. [BACKEND] FastAPI Backend")
            backend_idx = idx
        else:
            backend_idx = None
        
        print(f"  0. Exit\n")
        
        # Get user choice
        try:
            choice = int(input("Select an option: "))
            
            if choice == 0:
                print("👋 Goodbye!")
                return
            
            if backend_idx and choice == backend_idx:
                launch_backend()
            elif 1 <= choice <= len(options):
                typ, name = options[choice - 1]
                if typ == 'html':
                    launch_html(name)
                elif typ == 'gradio':
                    launch_gradio(name)
                elif typ == 'streamlit':
                    launch_streamlit(name)
            else:
                print("❌ Invalid option")
        except (ValueError, KeyboardInterrupt):
            print("\n👋 Goodbye!")
            return

def main():
    if len(sys.argv) < 2:
        interactive_menu()
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
