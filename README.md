# Our Story — Netflix Anniversary Website

A Netflix-themed anniversary website for your special person. 🎬❤️

## Pages

| Page | File | Description |
|------|------|-------------|
| Intro | `index.html` | Netflix "N" logo animation |
| Profiles | `profiles.html` | "Who's Watching?" — your monthly milestones |
| Browse | `browse.html` | Main Netflix-style gallery |
| Player | `player.html` | Slideshow of your photos with player controls |
| Credits | `credits.html` | Movie-style rolling credits |

---

## How to Personalize

### 1. Edit `js/config.js`

Open `js/config.js` and fill in your details:

```js
yourName:    "Aryan",          // your name
partnerName: "Jia",            // partner's name
showTitle:   "Our Story",
startDate:   "February 2026",
favoriteLocation: "Marine Drive",
```

### 2. Add Your Photos

Drop photos into these folders and name them accordingly:

```
images/
  hero.jpg                   ← main featured photo (browse page hero)
  profiles/
    month-1.jpg              ← Month 1 profile
    month-2.jpg              ← Month 2 profile
    month-3.jpg              ← Month 3 profile (anniversary)
  gallery/
    1.jpg  2.jpg  3.jpg ...  ← gallery photos (browse page + slideshow)
```

You can also update the filenames in `js/config.js` to match whatever you name them.

### 3. Update Gallery Titles

In `js/config.js`, update the `gallery` array with your own titles and photo files:

```js
gallery: [
  { src: "images/gallery/1.jpg", title: "Our First Date", category: "popular" },
  { src: "images/gallery/2.jpg", title: "Coffee Date",    category: "popular" },
  ...
]
```

---

## Hosting on GitHub Pages

1. Create a new GitHub repository (e.g., `our-story`)
2. Push all these files to the `main` branch
3. Go to **Settings → Pages**
4. Under **Source**, choose `main` branch and `/ (root)` folder
5. Click **Save** — your site will be live at `https://yourusername.github.io/our-story/`

---

## Flow

```
index.html  →  profiles.html  →  browse.html  →  player.html  →  credits.html
(N intro)      (Who's watching?)  (Netflix UI)    (Slideshow)     (Movie credits)
```

## Tips

- The site looks great on both desktop and mobile
- Keyboard shortcuts on the player page: `Space` = play/pause, `→` / `←` = next/prev photo, `Esc` = back
- Photos show as beautiful gradient placeholders until you add real images
- All photos are private — they only live in your GitHub repo
