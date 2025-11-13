# 🎵 Apple Music Integration Setup Guide

This guide helps you add Apple Music integration to your GitHub profile, displaying your currently playing or recently played tracks.

## Features

- ✅ Displays currently playing or recently played track
- ✅ Shows album artwork, track info, and metadata
- ✅ Updates automatically every 15 minutes
- ✅ Includes artist, album, genre, and duration
- ✅ Links directly to tracks on Apple Music
- ✅ Retry logic for reliability
- ✅ Graceful fallback if API is unavailable

## Setup Instructions

### Step 1: Get Apple Music API Credentials

1. **Join Apple Developer Program** (if not already a member)
   - Visit: https://developer.apple.com/programs/
   - Free for personal use with limitations

2. **Get MusicKit API Key**
   - Go to: https://developer.apple.com/account/resources/authkeys/list
   - Click "+" to create a new key
   - Enable "MusicKit" service
   - Download the `.p8` key file
   - Note your Key ID and Team ID

3. **Generate JWT Token**
   - Use your private key to generate a JSON Web Token
   - Tools: https://github.com/pelauimagineering/apple-music-token-generator
   - Or use online JWT generators with Apple Music template

### Step 2: Get User Music Token

You need a Music User Token to access your personal listening history:

1. **Developer Token**: Create from your API key (JWT)
2. **User Token**: Authorize with your Apple ID
   - Use Apple's MusicKit JS authorization
   - Or use this tool: https://music-user-token.herokuapp.com/

### Step 3: Add Secrets to Repository

Go to your profile repository (`JET609/JET609`):

1. Navigate to **Settings** > **Secrets and variables** > **Actions**
2. Click **New repository secret**
3. Add these secrets:

   ```
   Name: APPLE_MUSIC_API_KEY
   Value: [Your JWT/Developer Token]
   
   Name: APPLE_MUSIC_USER_TOKEN
   Value: [Your Music User Token]
   ```

### Step 4: Add Markers to README.md

Edit your profile README (`JET609/JET609/README.md`) and add these markers where you want the Apple Music section:

```markdown
<!--APPLE_MUSIC_START-->
<!--APPLE_MUSIC_END-->
```

Example placement:

```markdown
# Hi, I'm JET609! 👋

Some intro text...

<!--APPLE_MUSIC_START-->
<!--APPLE_MUSIC_END-->

## More sections...
```

### Step 5: Copy Workflow to Profile Repository

Copy `.github/workflows/apple-music.yml` from this repo to your profile repo (`JET609/JET609`):

```bash
# In your profile repository
mkdir -p .github/workflows
# Copy the apple-music.yml file
```

### Step 6: Test the Workflow

1. Go to **Actions** tab in your profile repository
2. Select **Apple Music Profile Integration**
3. Click **Run workflow**
4. Check the logs for any errors
5. Verify your README is updated

## What It Looks Like

### With Music Playing:

```markdown
### 🎵 Currently Listening

![Album Art](album-artwork-url)

**[Track Name](apple-music-link)**  
by **Artist Name**

📀 Album: Album Name  
🎸 Genre: Pop  
⏱️ Duration: 3:45

Last updated: 2025-11-13 12:00 UTC
```

### Without Configuration:

```markdown
### 🎵 Apple Music

🎵 Apple Music - Setup Required

Configure API credentials to display your music
```

## Troubleshooting

### No Recent Tracks Shown

- Make sure you've played music recently (within last few hours)
- Check that your Apple Music account is active
- Verify your User Token hasn't expired

### API Errors

- **401 Unauthorized**: Check your API credentials
- **403 Forbidden**: User Token may be invalid
- **404 Not Found**: No recent listening history

### Workflow Not Running

- Check if workflow file is in `.github/workflows/` directory
- Verify GitHub Actions is enabled in repository settings
- Check for any syntax errors in YAML file

### README Not Updating

- Ensure markers `<!--APPLE_MUSIC_START-->` and `<!--APPLE_MUSIC_END-->` exist
- Check workflow logs for errors
- Verify bot has write permissions

## Customization

### Change Update Frequency

Edit the cron schedule in `apple-music.yml`:

```yaml
schedule:
  - cron: "*/15 * * * *"  # Every 15 minutes
  - cron: "*/30 * * * *"  # Every 30 minutes
  - cron: "0 * * * *"     # Every hour
```

### Modify Display Style

Edit the `music_section` generation in the Python script to customize:
- Layout and formatting
- Which metadata to display
- Emoji usage
- Link formats

### Add More Features

You can extend the workflow to:
- Show top tracks of the week
- Display playlists
- Show listening statistics
- Add genre distribution
- Include play counts

## Alternative: Spotify Integration

If you prefer Spotify, check out these popular alternatives:
- [spotify-github-profile](https://github.com/kittinan/spotify-github-profile)
- [novatorem](https://github.com/novatorem/novatorem)

## Rate Limits

Apple Music API has rate limits:
- **Developer Token**: 20,000 requests per day
- **User Token**: Varies by account type
- This workflow uses ~96 requests per day (every 15 min)

## Security Notes

⚠️ **Important**: 
- Never commit API keys directly in code
- Always use repository secrets
- Tokens are only accessible to workflow runs
- User Token may expire (typically after 6 months)
- Regenerate tokens periodically for security

## Resources

- [Apple Music API Docs](https://developer.apple.com/documentation/applemusicapi)
- [MusicKit Documentation](https://developer.apple.com/documentation/musickit)
- [Apple Developer Portal](https://developer.apple.com/)

## Support

If you encounter issues:
1. Check workflow logs in Actions tab
2. Verify all secrets are correctly set
3. Test API credentials independently
4. Review Apple Music API status

---

**Created**: 2025-11-13  
**Status**: Ready to Deploy  
**Maintenance**: Token refresh needed every 6 months
