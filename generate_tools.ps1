$tools = @(
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
)

$template = @"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{0} - MyTool</title>
    <link rel="stylesheet" href="../style.css">
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body data-tool="{1}">
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
                <h1>{0}</h1>
                <p>Professional {0} tool for everyday use.</p>
            </div>
        </div>

        <div class="container">
            <div class="tool-container">
                <div class="tool-controls">
                    <div id="tool-ui-placeholder">
                        <!-- Specific tool UI will be injected or handled by script.js -->
                        <p>This tool is ready to use. Please interact with the inputs below.</p>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <footer>
        <div class="container footer-bottom">
            <p>&copy; 2026 MyTool Platform. All rights reserved.</p>
        </div>
    </footer>

    <script src="../script.js"></script>
    <script>
        lucide.createIcons();
    </script>
</body>
</html>
"@

$toolsDir = "c:\Users\Administrator\.gemini\antigravity\playground\gravitic-ride\src\tools"
if (!(Test-Path $toolsDir)) { New-Item -ItemType Directory -Path $toolsDir }

foreach ($id in $tools) {
    $name = ($id -replace '-', ' ').ToUpper().Substring(0,1) + ($id -replace '-', ' ').Substring(1)
    $content = $template -f $name, $id
    $path = Join-Path $toolsDir ($id + ".html")
    Set-Content -Path $path -Value $content -Encoding utf8
}

Write-Host "Generated $($tools.Count) tool files."
