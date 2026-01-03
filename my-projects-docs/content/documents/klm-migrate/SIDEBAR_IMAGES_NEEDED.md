---
title: "SIDEBAR_IMAGES_NEEDED"
project: klm-migrate
original_path: klm-hugo-site/SIDEBAR_IMAGES_NEEDED.md
modified: 2025-12-28T18:58:16.661122
---

# Sidebar Images Needed

This document lists the sidebar images that need to be sourced from royalty-free image sites.

## Current Issues

The following pages are using incorrect sidebar images:

1. **Boat/Watercraft Insurance** (`content/boat-insurance.md`)
   - Currently using: `featured-commercial-insurance-thumbnail.png` (WRONG)
   - Needs: Boat/watercraft-specific sidebar image

2. **Umbrella Insurance** (`content/umbrella-insurance.md`)
   - Currently using: `featured-life-insurance-thumbnail.png` (WRONG)
   - Needs: Umbrella/protection-specific sidebar image

## Recommended Sources

### Free Royalty-Free Image Sites:

- **[Unsplash](https://unsplash.com/)** - Free commercial use, no attribution required
- **[Pexels](https://www.pexels.com/)** - Free commercial use, no attribution required

## Image Specifications

- **Dimensions**: Approximately 300-400px wide (will be displayed in sidebar)
- **Orientation**: Portrait or square preferred
- **Quality**: Professional, high-resolution
- **Style**: Clean, insurance-appropriate, matches brand aesthetic

## Search Terms & Download Instructions

### For Boat/Watercraft Insurance Sidebar:

**Search terms:** `boat water`, `sailing boat`, `yacht water`, `motorboat lake`

**Best options:**
1. Visit [Unsplash Boat Photos](https://unsplash.com/s/photos/boat)
2. Look for:
   - Clear, professional boat images
   - Good lighting and composition
   - Boats on water (not docked necessarily)
   - Family-friendly vessels (not race boats or extreme sports)
3. Download a suitable image
4. Rename to: `featured-boat-insurance-thumbnail.jpg` or `.png`
5. Place in: `static/images/`
6. Update `content/boat-insurance.md` line 6:
   ```
   sidebar_image: "/images/featured-boat-insurance-thumbnail.jpg"
   ```

**Suggested Unsplash images:**
- Search "boat family" for family-friendly watercraft
- Search "sailboat peaceful" for leisure boats
- Search "fishing boat" for sport fishing coverage imagery

### For Umbrella Insurance Sidebar:

**Search terms:** `umbrella protection`, `red umbrella`, `umbrella rain`, `umbrella security`

**Best options:**
1. Visit [Unsplash Umbrella Photos](https://unsplash.com/s/photos/umbrella)
2. Look for:
   - Single umbrella, preferably overhead/protection angle
   - Professional/metaphorical protection imagery
   - Clear, uncluttered composition
   - Colors that match site palette (blues, reds work well)
3. Download a suitable image
4. Rename to: `featured-umbrella-insurance-thumbnail.jpg` or `.png`
5. Place in: `static/images/`
6. Update `content/umbrella-insurance.md` line 6:
   ```
   sidebar_image: "/images/featured-umbrella-insurance-thumbnail.jpg"
   ```

**Suggested Unsplash images:**
- Search "umbrella overhead" for protection metaphor
- Search "red umbrella rain" for classic insurance imagery
- Search "umbrella shelter" for security concept

## Quick Commands

After downloading images:

```bash
# Move downloaded images to static/images/
mv ~/Downloads/your-boat-image.jpg static/images/featured-boat-insurance-thumbnail.jpg
mv ~/Downloads/your-umbrella-image.jpg static/images/featured-umbrella-insurance-thumbnail.jpg

# Update content files (done via Edit tool or manually)
# Test locally
hugo server -D

# View at http://localhost:1313/boat-insurance/ and /umbrella-insurance/
```

## Alternative: Use Pexels

If Unsplash doesn't have ideal images:

- **Boat images**: [Pexels Boat Search](https://www.pexels.com/search/boat/)
- **Umbrella images**: [Pexels Umbrella Search](https://www.pexels.com/search/umbrella/)

Both offer the same free commercial license.

---

**Status**: Waiting for image downloads
**Updated**: December 28, 2025
