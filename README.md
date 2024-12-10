# Coding Pirates Præsentationer

Dette repository indeholder præsentationer for Coding Pirates Midtfyn.

## Opsætning

1. Installer reveal-md:  
   ```bash
   npm install -g reveal-md
   ```

## Struktur for Præsentationer

Hver præsentation skal ligge i en mappe navngivet efter datoen (YYYY-MM-DD) og indeholde:  
- `deck.md` - Præsentationens indhold  
- `images/` - Billeder brugt i præsentationen  
- `code/` - Eventuelle kodeeksempler (valgfrit)  

## Generér Præsentationer

Kør genereringsscriptet:  
```bash
./generate.sh
```

Dette vil:  
1. Oprette en `dist`-mappe med alle præsentationer  
2. Generere en `index.html` med links til alle præsentationer  
3. Anvende det delte tema på alle præsentationer  

## Se Præsentationer

Efter genereringen kan du åbne `dist/index.html` i din browser for at se alle tilgængelige præsentationer.
