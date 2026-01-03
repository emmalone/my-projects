---
title: "claude"
project: mouse
original_path: claude.md
modified: 2026-01-02T23:16:52.121467
---

# Mouse Natural Scrolling Toggle - Project Context

**macOS MenuBar Application for Quick Natural Scrolling Control**

---

## 📋 Quick Reference

**Project Location:** `/Users/mark/PycharmProjects/mouse`
**Developer:** Mark (mark@emm-associates.com)
**Purpose:** MenuBar app with keyboard shortcut to toggle natural scrolling on/off
**Last Updated:** January 2, 2026

---

## 🎯 Project Purpose

A simple macOS menubar application that allows quick toggling of "natural scrolling" direction using:
- **Keyboard Shortcut:** Command+0
- **MenuBar Icon:** 🖱️ click to toggle

---

## 📂 Project Structure

```
/Users/mark/PycharmProjects/mouse/
├── claude.md                        # This file - project context
├── menubar_toggle.py                # Main menubar application
├── configure_shortcut.py            # Keyboard shortcut configuration
├── install.py                       # Installation script
├── launch_menubar_app.command       # Launch script
│
└── Documentation:
    ├── QUICK_START.txt              # Quick start guide
    ├── HOWTO.txt                    # How-to guide
    ├── AFTER_REBOOT.txt             # Post-reboot instructions
    ├── FINAL_SETUP.txt              # Setup instructions
    ├── INSTALLATION_STATUS.txt      # Installation status
    └── KEYBOARD_SHORTCUT_SETUP.txt  # Keyboard shortcut setup
```

---

## ⚙️ How It Works

### Main Components

1. **menubar_toggle.py**
   - Creates menubar icon (🖱️)
   - Listens for Command+0 keyboard shortcut
   - Toggles natural scrolling via system preferences
   - Shows notification when toggling

2. **configure_shortcut.py**
   - Sets up global keyboard shortcut (Command+0)
   - Requires accessibility permissions

3. **install.py**
   - Installs dependencies
   - Configures launch agent
   - Sets up auto-start on login

---

## 🚀 Usage

### Quick Start
```bash
# Look for 🖱️ icon in menu bar (top right)
# Press Command+0 to toggle natural scrolling
```

### Manual Launch
```bash
cd /Users/mark/PycharmProjects/mouse
python3 menubar_toggle.py &
```

### Check Logs
```bash
cat /tmp/naturalscrolling.log
cat /tmp/naturalscrolling.error.log
```

---

## 🔧 Technical Details

### Dependencies
- Python 3
- rumps (menubar app framework)
- pynput (keyboard shortcuts)
- subprocess (system commands)

### System Requirements
- macOS
- Accessibility permissions (for keyboard shortcuts)
- System Preferences access (for toggling natural scrolling)

### How Toggle Works
```bash
# Get current natural scrolling state
defaults read NSGlobalDomain com.apple.swipescrolldirection

# Toggle it
defaults write NSGlobalDomain com.apple.swipescrolldirection -bool <true/false>
```

---

## 📝 Recent Work History

### Initial Development
- ✅ Created menubar application with icon
- ✅ Implemented Command+0 keyboard shortcut
- ✅ Added natural scrolling toggle functionality
- ✅ Added notifications for user feedback
- ✅ Set up auto-launch on login
- ✅ Created comprehensive documentation

---

## 🐛 Troubleshooting

### MenuBar Icon Doesn't Appear
```bash
# Manually launch the app
python3 /Users/mark/PycharmProjects/mouse/menubar_toggle.py &
```

### Command+0 Not Working
- Check that app has Accessibility permissions
- System Preferences → Security & Privacy → Privacy → Accessibility
- Make sure "Terminal" or "Python" is enabled

### Toggle Not Changing Settings
- Check logs: `cat /tmp/naturalscrolling.log`
- Verify system preferences access
- Try manual toggle via menubar icon click

---

## 💡 Future Enhancements

Potential improvements:
- [ ] Custom keyboard shortcut configuration
- [ ] Different scrolling speeds
- [ ] Per-application scrolling settings
- [ ] Visual indicator of current state

---

## 📞 Support & Contact

**Developer Contact:**
- Mark
- Email: mark@emm-associates.com

**For Claude Code Sessions:**
- This file (`claude.md`) contains all project context
- Reference specific sections as needed
- Update this file after major changes

---

**Project Status:** Stable - Working as designed
**Current Phase:** Production use
**Last Updated:** January 2, 2026

---
