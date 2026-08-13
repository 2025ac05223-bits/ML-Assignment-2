# Streamlit Cloud Deployment Guide

## Overview

This guide will help you deploy your Breast Cancer Classification Model Comparison app to Streamlit Cloud for free hosting and public access.

## Prerequisites

✓ GitHub repository with your code
✓ Streamlit app (streamlit_app.py)
✓ requirements.txt with all dependencies
✓ Streamlit Cloud account (free)

## Step 1: Ensure Code is Pushed to GitHub

Your code must be on GitHub first. If not pushed yet:

```bash
cd "d:\BITS_WILP\Sem 1\ML\Assignment 2"
git push -u origin main
```

Verify your repository is live at:
```
https://github.com/2025ac05223-bits/ML-Assignment-2
```

## Step 2: Create Streamlit Cloud Account

1. Go to https://streamlit.io/cloud
2. Click "Sign up"
3. Choose to sign in with GitHub
4. Authorize Streamlit to access your GitHub account
5. Complete account setup

## Step 3: Deploy Your App

### Method A: Deploy from Streamlit Cloud Dashboard (Easiest)

1. Go to https://share.streamlit.io/
2. Click "New app"
3. Fill in the details:
   - **GitHub account:** 2025ac05223-bits
   - **Repository:** ML-Assignment-2
   - **Branch:** main
   - **Main file path:** streamlit_app.py
4. Click "Deploy"

### Method B: Deploy Directly from GitHub

1. Go to your repository: https://github.com/2025ac05223-bits/ML-Assignment-2
2. Look for Streamlit deployment option (if available)
3. Click deploy
4. Follow the prompts

## Step 4: Wait for Deployment

Streamlit will:
- Install all dependencies from requirements.txt
- Start your app
- Assign a unique URL

This usually takes 2-5 minutes for the first deployment.

## Step 5: Access Your Deployed App

Once deployed, your app will be available at a URL like:
```
https://ml-assignment-2-abcd1234.streamlit.app
```

Or find it on your Streamlit Cloud dashboard.

## Configuration Files Included

### .streamlit/config.toml
Located in `.streamlit/config.toml`, this file configures:

```toml
[theme]
base = "light"
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[client]
layoutMode = "centered"
maxUploadSize = 200

[server]
port = 8501
headless = true
enableXsrfProtection = true
enableCORS = true

[logger]
level = "info"
```

### requirements.txt
Includes all necessary packages:
- streamlit >= 1.28.0
- scikit-learn >= 1.3.0
- pandas >= 1.5.0
- numpy >= 1.24.0
- matplotlib >= 3.7.0
- seaborn >= 0.12.0
- joblib >= 1.3.0

## Troubleshooting

### App crashes on startup
- Check requirements.txt has all needed packages
- Verify streamlit_app.py is the correct file name
- Look at deployment logs for error messages

### "Module not found" errors
- Add missing package to requirements.txt
- Format: `package-name>=version`
- Redeploy to update dependencies

### App loads but doesn't display correctly
- Check Streamlit configuration in .streamlit/config.toml
- Verify all data files are in repository
- Check file paths are correct (use relative paths)

### Slow startup
- First deployment is slower as dependencies install
- Subsequent runs use cache
- Large ML models (like ours) may take longer to load

### "Memory exceeded"
- ML model training takes resources
- Streamlit Cloud has memory limits
- Use `@st.cache_resource` decorator (already used)

## Features Deployed

Your deployment includes:

✓ **5 ML Classification Models**
- Logistic Regression
- Decision Tree
- K-Nearest Neighbors
- Gaussian Naive Bayes
- Random Forest

✓ **6 Evaluation Metrics**
- Accuracy
- AUC Score
- Precision
- Recall
- F1 Score
- Matthews Correlation Coefficient

✓ **Interactive Visualizations**
- Model comparison charts
- Metrics heatmap
- Performance highlights

✓ **Dataset Information**
- Breast Cancer dataset (569 samples)
- 30 features
- Binary classification

## Managing Your Deployment

### Update Your App

To update your app on Streamlit Cloud:

1. Make code changes locally
2. Commit changes: `git commit -m "Update app"`
3. Push to GitHub: `git push`
4. Streamlit automatically redeploys

No manual redeployment needed - it watches your GitHub repo!

### View Deployment Logs

1. Go to https://share.streamlit.io/
2. Find your app
3. Click the three dots (⋮) menu
4. Select "View logs"

### Control Deployment Settings

1. Go to your app on Streamlit Cloud
2. Click the three dots (⋮) menu
3. Select "Settings"
4. Configure:
   - Python version
   - Run behavior
   - Notifications
   - Memory limits

### Reboot App

1. Go to your app on Streamlit Cloud
2. Click the three dots (⋮) menu
3. Select "Reboot app"

## Security Considerations

### API Keys and Secrets

Never commit secrets! Use Streamlit secrets instead:

1. Go to your app settings on Streamlit Cloud
2. Click "Secrets"
3. Add secrets in TOML format:
   ```toml
   api_key = "your-secret-key"
   database_url = "your-connection-string"
   ```

4. Access in code:
   ```python
   import streamlit as st
   secret = st.secrets["api_key"]
   ```

### Environment Variables

For local development, create `.streamlit/secrets.toml`:
```toml
# .streamlit/secrets.toml (add to .gitignore!)
api_key = "dev-key"
```

## Sharing Your App

Once deployed, share the URL:
```
https://ml-assignment-2-abcd1234.streamlit.app
```

People can:
- Access without installation
- Use the full interactive app
- Export results
- Share with others

## Monitoring and Statistics

Streamlit Cloud provides:
- Deployment status
- Error logs
- App usage statistics
- Performance metrics
- CPU and memory usage

Access these in your Streamlit Cloud dashboard.

## Customization

### Change App Icon and Title

Edit `streamlit_app.py`:
```python
st.set_page_config(
    page_title="Breast Cancer Classifier",
    page_icon="🏥",
    layout="wide"
)
```

### Add Custom Styling

Add to `streamlit_app.py`:
```python
st.markdown("""
    <style>
    .stHeader {
        color: #FF6B6B;
    }
    </style>
""", unsafe_allow_html=True)
```

### Add Authentication (Optional)

Use streamlit-authenticator:
```bash
pip install streamlit-authenticator
```

Then implement in your app for private access.

## Advanced Features

### Custom Domain

- Go to app settings on Streamlit Cloud
- Add custom domain
- Requires DNS configuration

### CI/CD Integration

- Streamlit automatically deploys on push
- Set up status checks in GitHub
- Disable auto-deploy if needed

### Analytics

- Enable in Streamlit Cloud settings
- Track user sessions
- Monitor performance

## Pricing

Streamlit Cloud is **FREE** for public apps!

- Unlimited apps
- Unlimited deployments
- Automatic HTTPS
- Custom domains (paid feature)

## Next Steps

1. **Push to GitHub** (if not already done)
   ```bash
   git push -u origin main
   ```

2. **Create Streamlit Cloud Account**
   - Go to https://streamlit.io/cloud
   - Sign up with GitHub

3. **Deploy App**
   - Go to https://share.streamlit.io/
   - Click "New app"
   - Select your repository and branch
   - Click "Deploy"

4. **Access Your Live App**
   - Get the unique URL
   - Share with others
   - Monitor deployments

## Resources

- **Streamlit Docs:** https://docs.streamlit.io/
- **Streamlit Cloud Docs:** https://docs.streamlit.io/streamlit-cloud
- **GitHub Integration:** https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app
- **Deployment Guide:** https://docs.streamlit.io/streamlit-cloud/get-started/quickstart

## Support

If you encounter issues:

1. Check Streamlit Cloud logs
2. Review Streamlit documentation
3. Check GitHub issues
4. Post in Streamlit forums

---

**Your App is Ready for Streamlit Cloud Deployment! 🚀**

Repository: https://github.com/2025ac05223-bits/ML-Assignment-2
App File: streamlit_app.py
Config: .streamlit/config.toml
Dependencies: requirements.txt
