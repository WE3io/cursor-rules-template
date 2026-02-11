#!/bin/bash

# Create output directory if it doesn't exist
mkdir -p output

# Create a new file for the combined content
output_file="output/combined_content.html"

# Add HTML header
echo "<!DOCTYPE html>
<html>
<head>
    <title>Combined AI Blindspots Content</title>
</head>
<body>" > "$output_file"

# Process each HTML file
for file in docs/ai-blindspots/*.html; do
    # Extract filename for the separator
    filename=$(basename "$file")
    
    # Add separator with filename
    echo "<hr><h2>Content from: $filename</h2>" >> "$output_file"
    
    # Extract content between body tags and append to output file
    sed -n '/<body>/,/<\/body>/p' "$file" | sed '1d;$d' >> "$output_file"
done

# Add HTML footer
echo "</body>
</html>" >> "$output_file"

echo "Content has been combined into $output_file" 