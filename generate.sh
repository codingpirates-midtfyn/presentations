#!/bin/bash

# Create dist directory if it doesn't exist
mkdir -p dist

# Copy theme file to dist
cp theme.css dist/

# Generate presentations for each folder
for dir in $(ls -d 20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]); do
  echo "Generating presentation for $dir"
  reveal-md "$dir/deck.md" --static "dist/$dir"
  cp -r "$dir/images" "dist/$dir/" 2>/dev/null || true
  cp -r "$dir/code" "dist/$dir/" 2>/dev/null || true
done

# Generate index.html
cat > dist/index.html << EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coding Pirates Presentations</title>
    <style>
        body {
            font-family: system-ui, -apple-system, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }
        h1 { color: #2d5986; }
        .presentations {
            list-style: none;
            padding: 0;
        }
        .presentations li {
            margin: 20px 0;
            padding: 15px;
            background: #f5f5f5;
            border-radius: 8px;
        }
        a {
            color: #2d5986;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Coding Pirates Presentations</h1>
    <ul class="presentations">
EOF

# Add links to each presentation
for dir in $(ls -d dist/20[0-9][0-9]-[0-9][0-9]-[0-9][0-9] | sort -r); do
    date=$(basename $dir)
    echo "        <li><a href=\"$date/deck.html\">Presentation $date</a></li>" >> dist/index.html
done

# Close HTML
cat >> dist/index.html << EOF
    </ul>
</body>
</html>
EOF

echo "All presentations generated in dist/ directory" 