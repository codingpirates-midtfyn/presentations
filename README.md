# Coding Pirates Præsentationer

Dette repository indeholder præsentationer for Coding Pirates Midtfyn.

## Opsætning

1. Install reveal-md:
```bash
npm install -g reveal-md
```

2. Each presentation should be in a folder named with the date (YYYY-MM-DD) and contain:
   - `deck.md` - The presentation content
   - `images/` - Images used in the presentation
   - `code/` - Any code examples (optional)

## Generate Presentations

Run the generation script:
```bash
./generate.sh
```

This will:
1. Create a `dist` directory with all presentations
2. Generate an index.html with links to all presentations
3. Apply the shared theme to all presentations

## View Presentations

After generating, open `dist/index.html` in your browser to see all available presentations.