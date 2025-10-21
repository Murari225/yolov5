# 🚀 Google Cloud Run Deployment Guide

Complete guide to deploy your YOLOv5 Web Application to Google Cloud Run.

## 📋 Prerequisites

1. **Google Cloud Account** (Free tier available)
   - Sign up at: https://cloud.google.com/
   - $300 free credit for new users

2. **Google Cloud SDK** installed
   - Download: https://cloud.google.com/sdk/docs/install
   - Or use Cloud Shell (browser-based)

3. **Docker** installed (optional, Cloud Build handles this)
   - Download: https://www.docker.com/products/docker-desktop

## 🎯 Step-by-Step Deployment

### **Step 1: Set Up Google Cloud Project**

```bash
# Login to Google Cloud
gcloud auth login

# Create a new project (or use existing)
gcloud projects create yolov5-webapp-project --name="YOLOv5 Web App"

# Set the project
gcloud config set project yolov5-webapp-project

# Enable required APIs
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable containerregistry.googleapis.com
```

### **Step 2: Configure Billing**

1. Go to: https://console.cloud.google.com/billing
2. Link your project to a billing account
3. (Required even for free tier)

### **Step 3: Build and Deploy**

#### **Option A: Using gcloud CLI (Recommended)**

```bash
# Navigate to your project directory
cd "C:\Users\pitha\OneDrive\Documents\New Folder\yolov5"

# Deploy to Cloud Run (builds automatically)
gcloud run deploy yolov5-webapp \
  --source . \
  --region us-central1 \
  --platform managed \
  --allow-unauthenticated \
  --memory 2Gi \
  --cpu 2 \
  --timeout 300 \
  --max-instances 10
```

#### **Option B: Using Docker + Cloud Build**

```bash
# Build the Docker image
gcloud builds submit --tag gcr.io/yolov5-webapp-project/yolov5-webapp

# Deploy to Cloud Run
gcloud run deploy yolov5-webapp \
  --image gcr.io/yolov5-webapp-project/yolov5-webapp \
  --region us-central1 \
  --platform managed \
  --allow-unauthenticated \
  --memory 2Gi \
  --cpu 2 \
  --timeout 300
```

#### **Option C: Using Cloud Build YAML**

```bash
# Deploy using cloudbuild.yaml
gcloud builds submit --config cloudbuild.yaml
```

### **Step 4: Access Your Application**

After deployment completes, you'll get a URL like:

```
https://yolov5-webapp-xxxxxxxxxx-uc.a.run.app
```

Open this URL in your browser to access your app!

## ⚙️ Configuration Options

### **Memory & CPU**

```bash
# Increase memory (for larger models)
--memory 4Gi

# Increase CPU
--cpu 4

# Options: 1, 2, 4, 8 CPUs
# Memory: 256Mi, 512Mi, 1Gi, 2Gi, 4Gi, 8Gi, 16Gi, 32Gi
```

### **Scaling**

```bash
# Set minimum instances (keeps app warm)
--min-instances 1

# Set maximum instances
--max-instances 10

# Concurrency (requests per instance)
--concurrency 80
```

### **Timeout**

```bash
# Maximum request timeout (up to 3600 seconds)
--timeout 300
```

### **Region**

```bash
# Choose closest region
--region us-central1     # Iowa, USA
--region us-east1        # South Carolina, USA
--region europe-west1    # Belgium
--region asia-southeast1 # Singapore
```

## 💰 Cost Estimation

**Free Tier (per month):**

- 2 million requests
- 360,000 GB-seconds
- 180,000 vCPU-seconds
- 1 GB network egress

**Estimated Costs (after free tier):**

- **2Gi memory, 2 CPU**: ~$0.00002400 per second
- **Average request (5 seconds)**: ~$0.00012
- **1000 requests/month**: ~$0.12
- **10,000 requests/month**: ~$1.20

**Tips to reduce costs:**

- Set `--min-instances 0` (cold starts but cheaper)
- Use smaller memory/CPU if possible
- Set appropriate timeout values

## 🔧 Troubleshooting

### **Build Fails**

```bash
# Check build logs
gcloud builds list
gcloud builds log [BUILD_ID]

# Common fixes:
# 1. Ensure requirements_deploy.txt exists
# 2. Check Dockerfile syntax
# 3. Verify all files are present
```

### **Deployment Fails**

```bash
# Check Cloud Run logs
gcloud run services logs read yolov5-webapp --region us-central1

# Common issues:
# 1. Port must be 8080 (or use $PORT env variable)
# 2. Memory too low (increase to 2Gi or 4Gi)
# 3. Timeout too short (increase to 300)
```

### **App Crashes**

```bash
# View real-time logs
gcloud run services logs tail yolov5-webapp --region us-central1

# Common fixes:
# 1. Increase memory: --memory 4Gi
# 2. Increase timeout: --timeout 600
# 3. Check model loading issues
```

### **Camera Not Working**

- **HTTPS Required**: Cloud Run provides HTTPS by default ✅
- **Browser Permissions**: Users must allow camera access
- **WebRTC**: Fully supported on Cloud Run

## 🔄 Update Deployment

```bash
# After making changes, redeploy
gcloud run deploy yolov5-webapp \
  --source . \
  --region us-central1

# Or with specific image
gcloud builds submit --tag gcr.io/yolov5-webapp-project/yolov5-webapp
gcloud run deploy yolov5-webapp \
  --image gcr.io/yolov5-webapp-project/yolov5-webapp \
  --region us-central1
```

## 🌐 Custom Domain (Optional)

```bash
# Map custom domain
gcloud run domain-mappings create \
  --service yolov5-webapp \
  --domain yourdomain.com \
  --region us-central1

# Follow DNS instructions provided
```

## 📊 Monitoring

### **View Metrics**

1. Go to: https://console.cloud.google.com/run
2. Click on your service
3. View metrics: requests, latency, memory, CPU

### **Set Up Alerts**

```bash
# Create alert for high error rate
gcloud alpha monitoring policies create \
  --notification-channels=CHANNEL_ID \
  --display-name="High Error Rate" \
  --condition-display-name="Error rate > 5%" \
  --condition-threshold-value=0.05
```

## 🔒 Security

### **Require Authentication**

```bash
# Deploy with authentication required
gcloud run deploy yolov5-webapp \
  --source . \
  --region us-central1 \
  --no-allow-unauthenticated

# Grant access to specific users
gcloud run services add-iam-policy-binding yolov5-webapp \
  --member='user:email@example.com' \
  --role='roles/run.invoker' \
  --region us-central1
```

### **Environment Variables**

```bash
# Set environment variables
gcloud run deploy yolov5-webapp \
  --set-env-vars "API_KEY=your-secret-key" \
  --region us-central1
```

## 📦 Files Created for Deployment

- ✅ **Dockerfile** - Container configuration
- ✅ **requirements_deploy.txt** - Python dependencies
- ✅ **cloudbuild.yaml** - Build configuration
- ✅ **app.yaml** - App Engine config (alternative)
- ✅ **.gcloudignore** - Files to exclude
- ✅ **DEPLOYMENT_GUIDE.md** - This guide

## 🎯 Quick Deploy Commands

```bash
# One-command deploy (easiest)
gcloud run deploy yolov5-webapp --source . --region us-central1 --allow-unauthenticated --memory 2Gi --cpu 2

# View service URL
gcloud run services describe yolov5-webapp --region us-central1 --format 'value(status.url)'

# Delete service (cleanup)
gcloud run services delete yolov5-webapp --region us-central1
```

## 📚 Additional Resources

- **Cloud Run Docs**: https://cloud.google.com/run/docs
- **Pricing Calculator**: https://cloud.google.com/products/calculator
- **Quickstarts**: https://cloud.google.com/run/docs/quickstarts
- **Best Practices**: https://cloud.google.com/run/docs/best-practices

## 🎉 Success Checklist

- [ ] Google Cloud account created
- [ ] gcloud CLI installed and authenticated
- [ ] Project created and billing enabled
- [ ] APIs enabled (Cloud Run, Cloud Build)
- [ ] Deployment command executed
- [ ] Service URL received
- [ ] Application accessible via URL
- [ ] Upload mode working
- [ ] Live camera working (HTTPS ✅)

---

**Need Help?** Check logs with:

```bash
gcloud run services logs tail yolov5-webapp --region us-central1
```

**Happy Deploying! 🚀**
