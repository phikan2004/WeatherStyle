---
name: weather-outfit
description: "Get clothing recommendations based on current weather for any location. Use when: user asks what to wear, outfit suggestions, or dressing for the weather. Fetches live weather via wttr.in and gives practical clothing advice."
homepage: https://github.com/phikan2004/WeatherStyle
metadata: { "openclaw": { "emoji": "👔", "requires": { "bins": ["curl"] } } }
---

# Weather Outfit Advisor

Fetch current weather for a location and recommend appropriate clothing.

## When to Use

✅ **USE this skill when:**

- "What should I wear today?"
- "What should I wear in [city]?"
- "Outfit for the weather in [location]"
- "Is it warm enough for shorts?"
- "Do I need a jacket?"

## When NOT to Use

❌ **DON'T use this skill when:**

- User only wants raw weather data → use the `weather` skill
- Historical weather or climate questions
- Severe weather alerts

## How to Fetch Weather

Always require a location. Use wttr.in to get current conditions:

```bash
# Current conditions as JSON (best for analysis)
curl -s "wttr.in/{CITY}?format=j1"

# Quick one-liner summary
curl -s "wttr.in/{CITY}?format=%l:+%c+%t+(feels+like+%f),+%h+humidity,+%p+precip"
```

Replace spaces in city names with `+`: `New+York`, `San+Francisco`, `Los+Angeles`

## Clothing Recommendation Guide

After fetching weather, recommend clothing based on **feels-like temperature**:

### Temperature Ranges

| Feels Like | Recommendation |
|---|---|
| Below 0°C / 32°F | Heavy winter coat, thermal base layer, sweater, warm pants, gloves, hat, scarf, insulated boots |
| 0–10°C / 32–50°F | Warm coat, sweater or hoodie, jeans or warm pants, scarf, light gloves |
| 10–16°C / 50–61°F | Light jacket or cardigan, long pants or jeans, could layer with a t-shirt underneath |
| 16–22°C / 61–72°F | Light layers — t-shirt with an optional light jacket, jeans or chinos |
| 22–28°C / 72–82°F | T-shirt, shorts or light pants, breathable fabrics |
| Above 28°C / 82°F | Lightweight t-shirt or tank top, shorts, sandals, sun hat if sunny |

### Adjust For Conditions

- **Rain / precipitation** → add waterproof jacket or umbrella
- **High wind** → add windbreaker or layer up
- **High humidity (>70%)** → lightweight, moisture-wicking, breathable fabrics
- **Snow** → waterproof boots, extra layers
- **Sunny** → sunglasses, sunscreen if hot

## Example Workflow

User: "What should I wear today in Chicago?"

```bash
curl -s "wttr.in/Chicago?format=j1"
```

Parse the response → get `FeelsLikeC` and weather description → apply the guide above → give a clear, friendly recommendation.

## Response Format

Keep responses concise and practical. Example:

> It's 8°C (feels like 4°C) in Chicago with light rain. I'd recommend:
> - Warm coat or insulated jacket
> - Sweater or hoodie underneath
> - Jeans or warm pants
> - Waterproof shoes and an umbrella
> - Scarf and light gloves
