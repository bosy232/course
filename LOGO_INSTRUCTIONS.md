# Logo Setup Instructions

## How to Add PICO Energy Logo

### Step 1: Prepare Your Logo
1. Make sure your logo is in PNG or SVG format
2. Recommended size: 200x80 pixels or similar aspect ratio
3. The logo should have a transparent background or be on a dark background

### Step 2: Add Logo to Public Folder
1. Copy your logo file to the `public` folder
2. Rename it to `logo.png` (or update the path in the code)
3. The file structure should look like:
   ```
   public/
   ├── logo.png          ← Your logo here
   ├── index.html
   ├── merged_employees.json
   └── ...
   ```

### Step 3: Update Logo Path (if needed)
If your logo has a different filename, update the path in `src/pages/EmployeePage.js`:

```javascript
<img 
  src="/your-logo-filename.png"  // Change this line
  alt="PICO Energy Logo" 
  className="company-logo"
  // ...
/>
```

### Step 4: Logo Styling
The logo is automatically styled to:
- Display in white color (using CSS filter)
- Maintain aspect ratio
- Be responsive on mobile devices
- Fall back to text logo if image fails to load

### Step 5: Test
1. Start the development server: `npm start`
2. Visit any employee page: `http://localhost:3000/employee/{code}`
3. Check that the logo appears correctly in the header

## Logo Specifications

- **Format**: PNG, SVG, or JPG
- **Size**: 200x80px recommended
- **Background**: Transparent or dark
- **Colors**: Will be converted to white automatically
- **Location**: `public/logo.png`

## Fallback
If the logo fails to load, the system will automatically show a text-based logo with "PICO Energy" text.

## Troubleshooting

### Logo not showing:
1. Check file path in `public` folder
2. Verify filename matches the `src` attribute
3. Check browser console for errors

### Logo appears colored instead of white:
- The CSS filter `brightness(0) invert(1)` converts the logo to white
- If your logo is already white, you can remove this filter

### Logo too large/small:
- Adjust the `height` property in `.company-logo` CSS class
- Current size: 40px height on desktop, 30px on mobile 