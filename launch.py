#!/usr/bin/env python3
import os
import sys
import webbrowser
import subprocess
import signal
from pathlib import Path

BASE_DIR = Path(__file__).parent

def find_examples():
    """Find all examples in the repo"""
    examples = {
        'landing': [],
        'blog': [],
        'portfolio': [],
        'shopping': []
    }
    
    # Landing page examples
    landing_dir = BASE_DIR / 'landing-pages'
    if landing_dir.exists():
        examples['landing'] = sorted([d.name for d in landing_dir.iterdir() if d.is_dir()])
    
    # Blog examples
    blog_dir = BASE_DIR / 'blog-pages'
    if blog_dir.exists():
        examples['blog'] = sorted([d.name for d in blog_dir.iterdir() if d.is_dir()])
    
    # Portfolio examples
    portfolio_dir = BASE_DIR / 'portfolio-pages'
    if portfolio_dir.exists():
        examples['portfolio'] = sorted([d.name for d in portfolio_dir.iterdir() if d.is_dir()])
    
    # Shopping examples
    shopping_dir = BASE_DIR / 'shopping-pages'
    if shopping_dir.exists():
        examples['shopping'] = sorted([d.name for d in shopping_dir.iterdir() if d.is_dir()])
    
    return examples

def list_examples():
    """List all available examples"""
    examples = find_examples()
    
    print("\n📦 Available Examples:\n")
    
    if examples['landing']:
        print("Landing Pages:")
        for ex in examples['landing']:
            print(f"  • {ex}")
    
    if examples['blog']:
        print("\nBlog Pages:")
        for ex in examples['blog']:
            print(f"  • {ex}")
    
    if examples['portfolio']:
        print("\nPortfolio Pages:")
        for ex in examples['portfolio']:
            print(f"  • {ex}")
    
    if examples['shopping']:
        print("\nShopping Pages:")
        for ex in examples['shopping']:
            print(f"  • {ex}")
    
    print("\n💡 Usage:")
    print("  ./launch.py landing <example-name>")
    print("  ./launch.py blog <example-name>")
    print("  ./launch.py portfolio <example-name>")
    print("  ./launch.py shopping <example-name>")
    print("  ./launch.py backend")

def launch_landing(example_name):
    """Launch landing page example"""
    example_path = BASE_DIR / 'landing-pages' / example_name
    
    if not example_path.exists():
        print(f"❌ Example '{example_name}' not found")
        return
    
    print(f"\n🚀 Launching {example_name}...")
    print("📡 Server running at http://localhost:8000")
    print("Press Ctrl+C to stop and return to menu\n")
    
    os.chdir(example_path)
    
    try:
        webbrowser.open('http://localhost:8000')
    except:
        pass
    
    process = None
    try:
        process = subprocess.Popen(['python3', '-m', 'http.server', '8000'])
        process.wait()
    except KeyboardInterrupt:
        if process:
            process.terminate()
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                process.kill()
        print("\n\n✅ Server stopped")

def launch_blog(example_name):
    """Launch blog page example"""
    example_path = BASE_DIR / 'blog-pages' / example_name
    
    if not example_path.exists():
        print(f"❌ Example '{example_name}' not found")
        return
    
    print(f"\n🚀 Launching {example_name}...")
    print("📡 Server running at http://localhost:8000")
    print("Press Ctrl+C to stop and return to menu\n")
    
    os.chdir(example_path)
    
    try:
        webbrowser.open('http://localhost:8000')
    except:
        pass
    
    process = None
    try:
        process = subprocess.Popen(['python3', '-m', 'http.server', '8000'])
        process.wait()
    except KeyboardInterrupt:
        if process:
            process.terminate()
        print("\n\n✅ Server stopped")

def launch_portfolio(example_name):
    """Launch portfolio page example"""
    example_path = BASE_DIR / 'portfolio-pages' / example_name
    
    if not example_path.exists():
        print(f"❌ Example '{example_name}' not found")
        return
    
    print(f"\n🚀 Launching {example_name}...")
    print("📡 Server running at http://localhost:8000")
    print("Press Ctrl+C to stop and return to menu\n")
    
    os.chdir(example_path)
    
    try:
        webbrowser.open('http://localhost:8000')
    except:
        pass
    
    process = None
    try:
        process = subprocess.Popen(['python3', '-m', 'http.server', '8000'])
        process.wait()
    except KeyboardInterrupt:
        if process:
            process.terminate()
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                process.kill()
        print("\n\n✅ Server stopped")

def launch_shopping(example_name):
    """Launch shopping page example"""
    example_path = BASE_DIR / 'shopping-pages' / example_name
    
    if not example_path.exists():
        print(f"❌ Example '{example_name}' not found")
        return
    
    print(f"\n🚀 Launching {example_name}...")
    print("📡 Server running at http://localhost:8000")
    print("Press Ctrl+C to stop and return to menu\n")
    
    os.chdir(example_path)
    
    try:
        webbrowser.open('http://localhost:8000')
    except:
        pass
    
    process = None
    try:
        process = subprocess.Popen(['python3', '-m', 'http.server', '8000'])
        process.wait()
    except KeyboardInterrupt:
        if process:
            process.terminate()
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                process.kill()
        print("\n\n✅ Server stopped")

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
        
        # Build menu options with prefix + number (e.g., l1, b1)
        options = {}  # prefix+number -> (type, name)
        prefixes = {
            'landing': 'l',
            'blog': 'b',
            'portfolio': 'p',
            'shopping': 'sh'
        }
        
        import re
        for typ in ['landing', 'blog', 'portfolio', 'shopping']:
            for ex in examples[typ]:
                # Extract number from name (e.g., landing-page-03 -> 3)
                match = re.search(r'-(\d+)$', ex)
                if match:
                    num = str(int(match.group(1)))  # Strip leading zeros
                    key = f"{prefixes[typ]}{num}"
                    options[key] = (typ, ex)
        
        # Check if backend exists
        backend_exists = (BASE_DIR / 'backend' / 'main.py').exists()
        
        if not options and not backend_exists:
            print("❌ No examples found")
            return
        
        print("\n🚀 Frontend Designs Launcher\n")
        
        # Display menu grouped by type
        section_names = {
            'landing': 'Landing Pages',
            'blog': 'Blog Pages',
            'portfolio': 'Portfolio Pages',
            'shopping': 'Shopping Pages'
        }
        
        for typ in ['landing', 'blog', 'portfolio', 'shopping']:
            if examples[typ]:
                print(f"{section_names[typ]}:")
                for ex in examples[typ]:
                    match = re.search(r'-(\d+)$', ex)
                    if match:
                        num = str(int(match.group(1)))  # Strip leading zeros
                        key = f"{prefixes[typ]}{num}"
                        print(f"  {key:>3}. {ex}")
                print()  # Blank line after each section
        
        if backend_exists:
            print("Backend:")
            print(f"   99. FastAPI Backend\n")
        
        print("   0. Exit\n")
        
        # Get user choice
        try:
            choice = input("Select an option: ").strip().lower()
            
            if choice == '0':
                print("👋 Goodbye!")
                return
            
            if backend_exists and choice == '99':
                launch_backend()
            elif choice in options:
                typ, name = options[choice]
                if typ == 'landing':
                    launch_landing(name)
                elif typ == 'blog':
                    launch_blog(name)
                elif typ == 'portfolio':
                    launch_portfolio(name)
                elif typ == 'shopping':
                    launch_shopping(name)
            else:
                print("❌ Invalid option")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            return

def main():
    if len(sys.argv) < 2:
        interactive_menu()
        return
    
    command = sys.argv[1]
    
    if command == 'list':
        list_examples()
    elif command == 'landing' and len(sys.argv) > 2:
        launch_landing(sys.argv[2])
    elif command == 'blog' and len(sys.argv) > 2:
        launch_blog(sys.argv[2])
    elif command == 'portfolio' and len(sys.argv) > 2:
        launch_portfolio(sys.argv[2])
    elif command == 'shopping' and len(sys.argv) > 2:
        launch_shopping(sys.argv[2])
    elif command == 'backend':
        launch_backend()
    else:
        print("❌ Invalid command")
        list_examples()

if __name__ == '__main__':
    main()
