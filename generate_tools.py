
import os

tools = [
    # Category 1: Calculator & Math
    {"id": "simple-calculator", "name": "Simple Calculator", "desc": "Basic arithmetic operations", "ui": '''
        <div class="tool-controls">
            <input type="text" id="calcDisplay" class="input-field" readonly style="text-align: right; font-size: 2rem; height: 60px;">
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-top: 1rem;">
                <button class="btn calc-btn" data-val="C" style="background: #ef4444;">C</button>
                <button class="btn calc-btn" data-val="/">/</button>
                <button class="btn calc-btn" data-val="*">*</button>
                <button class="btn calc-btn" data-val="-">-</button>
                <button class="btn calc-btn" data-val="7" style="background:#f1f5f9; color:#1e293b;">7</button>
                <button class="btn calc-btn" data-val="8" style="background:#f1f5f9; color:#1e293b;">8</button>
                <button class="btn calc-btn" data-val="9" style="background:#f1f5f9; color:#1e293b;">9</button>
                <button class="btn calc-btn" data-val="+">+</button>
                <button class="btn calc-btn" data-val="4" style="background:#f1f5f9; color:#1e293b;">4</button>
                <button class="btn calc-btn" data-val="5" style="background:#f1f5f9; color:#1e293b;">5</button>
                <button class="btn calc-btn" data-val="6" style="background:#f1f5f9; color:#1e293b;">6</button>
                <button class="btn calc-btn" data-val="=" style="grid-row: span 2; background: var(--accent);">=</button>
                <button class="btn calc-btn" data-val="1" style="background:#f1f5f9; color:#1e293b;">1</button>
                <button class="btn calc-btn" data-val="2" style="background:#f1f5f9; color:#1e293b;">2</button>
                <button class="btn calc-btn" data-val="3" style="background:#f1f5f9; color:#1e293b;">3</button>
                <button class="btn calc-btn" data-val="0" style="grid-column: span 2; background:#f1f5f9; color:#1e293b;">0</button>
                <button class="btn calc-btn" data-val="." style="background:#f1f5f9; color:#1e293b;">.</button>
            </div>
        </div>
    '''},
    {"id": "percentage-calculator", "name": "Percentage Calculator", "desc": "Calculate percentages easily", "ui": '''
        <div class="tool-controls">
            <div class="input-group">
                <label>What is</label>
                <div style="display:flex; gap:10px; align-items:center;">
                    <input type="number" id="perc1" class="input-field" placeholder="10">
                    <span>% of</span>
                    <input type="number" id="perc2" class="input-field" placeholder="100">
                </div>
            </div>
            <button class="btn" onclick="calcPerc()">Calculate</button>
            <div class="result-area">
                <span class="result-label">Result:</span>
                <span id="percResult" class="result-value">---</span>
            </div>
        </div>
        <script>
            function calcPerc() {
                const p = document.getElementById('perc1').value;
                const v = document.getElementById('perc2').value;
                document.getElementById('percResult').innerText = (p / 100 * v).toFixed(2);
            }
        </script>
    '''},
    {"id": "age-calculator", "name": "Age Calculator", "desc": "Calculate exact age from birthdate", "ui": '''
        <div class="tool-controls">
            <div class="input-group">
                <label>Select Birthdate</label>
                <input type="date" id="birthdate" class="input-field">
            </div>
            <button class="btn" id="calculateAge">Calculate Age</button>
            <div class="result-area">
                <span class="result-label">Your Age:</span>
                <span id="ageResult" class="result-value">---</span>
            </div>
        </div>
    '''},
    {"id": "bmi-calculator", "name": "BMI Calculator", "desc": "Calculate Body Mass Index", "ui": '''
        <div class="tool-controls">
            <div class="input-group">
                <label>Weight (kg)</label>
                <input type="number" id="weight" class="input-field" placeholder="70">
            </div>
            <div class="input-group">
                <label>Height (cm)</label>
                <input type="number" id="height" class="input-field" placeholder="175">
            </div>
            <button class="btn" id="calculateBMI">Calculate BMI</button>
            <div class="result-area">
                <span id="bmiResult" class="result-value">---</span>
            </div>
        </div>
    '''},
    # Category 2: Text
    {"id": "word-counter", "name": "Word Counter", "desc": "Count words and characters", "ui": '''
        <div class="tool-controls">
            <div class="input-group">
                <label>Enter Text</label>
                <textarea id="textInput" class="input-field" rows="8" placeholder="Paste your text here..."></textarea>
            </div>
            <div style="display:flex; gap:2rem; margin-top:1rem;">
                <div><strong>Words:</strong> <span id="wordCount">0</span></div>
                <div><strong>Characters:</strong> <span id="charCount">0</span></div>
            </div>
        </div>
    '''},
    {"id": "password-generator", "name": "Password Generator", "desc": "Generate strong random passwords", "ui": '''
        <div class="tool-controls">
            <div class="input-group">
                <label>Password Length</label>
                <input type="number" id="passLength" class="input-field" value="16" min="6" max="50">
            </div>
            <button class="btn" id="generatePass">Generate Password</button>
            <div class="result-area">
                <input type="text" id="passResult" class="input-field" readonly style="width:100%; border:none; background:transparent;">
            </div>
        </div>
    '''},
    # Category 3: Developer
    {"id": "json-formatter", "name": "JSON Formatter", "desc": "Format and validate JSON", "ui": '''
        <div class="tool-controls">
            <div class="input-group">
                <label>Input JSON</label>
                <textarea id="jsonInput" class="input-field" rows="8" placeholder='{"key": "value"}'></textarea>
            </div>
            <button class="btn" id="formatJSON">Format JSON</button>
            <div class="input-group" style="margin-top:1rem;">
                <label>Output</label>
                <textarea id="jsonOutput" class="input-field" rows="8" readonly></textarea>
            </div>
        </div>
    '''},
    # Category 5: Daily
    {"id": "todo-list", "name": "To-Do List", "desc": "Simple task management", "ui": '''
        <div class="tool-controls">
            <div style="display:flex; gap:10px;">
                <input type="text" id="todoInput" class="input-field" placeholder="Add a new task..." style="flex:1;">
                <button class="btn" id="addTodo">Add</button>
            </div>
            <ul id="todoList" style="list-style:none; margin-top:1.5rem; display:flex; flex-direction:column; gap:10px;">
                <!-- Todos go here -->
            </ul>
        </div>
        <style>
            #todoList li {
                display:flex; justify-content:space-between; align-items:center;
                background:#f8fafc; padding:10px 15px; border-radius:8px; border:1px solid #e2e8f0;
            }
            #todoList li button {
                background:#fee2e2; color:#ef4444; border:none; padding:5px 10px; border-radius:4px; cursor:pointer;
            }
        </style>
    '''},
]

# Standard template
template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - MyTool</title>
    <link rel="stylesheet" href="../style.css">
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body data-tool="{id}">
    <header>
        <div class="container nav">
            <a href="../index.html" class="logo"><i data-lucide="wrench"></i> MyTool</a>
            <ul class="nav-links">
                <li><a href="../index.html">Home</a></li>
                <li><a href="../about.html">About</a></li>
                <li><a href="../contact.html">Contact</a></li>
            </ul>
        </div>
    </header>

    <main>
        <div class="tool-header">
            <div class="container">
                <a href="../index.html" style="text-decoration:none; color:var(--primary); font-weight:500; display:flex; align-items:center; gap:5px; margin-bottom:1rem;">
                    <i data-lucide="arrow-left" style="width:18px;"></i> Back to Home
                </a>
                <h1>{name}</h1>
                <p>{desc}</p>
            </div>
        </div>

        <div class="container">
            <div class="tool-container">
                {ui}
            </div>
        </div>
    </main>

    <footer>
        <div class="container footer-bottom">
            <p>&copy; 2026 MyTool Platform. All rights reserved.</p>
        </div>
    </footer>

    <script src="../script.js"></script>
</body>
</html>"""

# Simplified tool list for the rest of 50 to fill the gaps
all_tool_ids = [
    "simple-calculator", "percentage-calculator", "age-calculator", "emi-calculator", "bmi-calculator",
    "discount-calculator", "profit-loss-calculator", "currency-converter", "scientific-calculator", "unit-converter",
    "word-counter", "character-counter", "case-converter", "remove-extra-spaces", "text-reverser",
    "password-generator", "random-name-picker", "lorem-ipsum-generator", "slug-generator", "text-to-binary",
    "json-formatter", "base64-encoder-decoder", "url-encoder-decoder", "html-minifier", "css-minifier",
    "js-minifier", "regex-tester", "timestamp-converter", "color-code-converter", "uuid-generator",
    "gradient-generator", "box-shadow-generator", "border-radius-generator", "qr-code-generator", "image-compressor",
    "image-to-base64", "favicon-generator", "svg-shape-generator", "color-palette-generator", "meme-generator",
    "todo-list", "countdown-timer", "pomodoro-timer", "habit-tracker", "daily-expense",
    "gpa-calculator", "calorie-calculator", "electricity-bill", "typing-speed-test", "random-quote"
]

processed_ids = [t["id"] for t in tools]

for tool_id in all_tool_ids:
    if tool_id not in processed_ids:
        # Create a basic stub for missing tools
        name = tool_id.replace('-', ' ').title()
        tools.append({
            "id": tool_id,
            "name": name,
            "desc": f"Professional {name} tool for everyday use.",
            "ui": f'''
                <div class="tool-controls">
                    <p>Tool {name} functionality is coming soon or implemented in script.js</p>
                    <div class="result-area">
                        <p>Work in Progress</p>
                    </div>
                </div>
            '''
        })

for tool in tools:
    filename = f"{tool['id']}.html"
    filepath = os.path.join("c:\\\\Users\\\\Administrator\\\\.gemini\\\\antigravity\\\\playground\\\\gravitic-ride\\\\src\\\\tools", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(template.format(**tool))

print(f"Generated {len(tools)} tool files.")
