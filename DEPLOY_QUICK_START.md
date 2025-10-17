# 🚀 Quick Deploy to Google Cloud Run

## ⚡ Super Fast Deployment (3 Steps)

### **Prerequisites:**
1. Google Cloud account (free $300 credit)
2. gcloud CLI installed

### **Deploy Now:**

```bash
# 1. Login
gcloud auth login

# 2. Set project (create one at console.cloud.google.com)
gcloud config set project YOUR_PROJECT_ID

# 3. Deploy (one command!)
gcloud run deploy yolov5-webapp --source . --region us-central1 --allow-unauthenticated --memory 2Gi --cpu 2
```

**That's it!** ✨

---

## 📋 Detailed Steps

### **1. Install gcloud CLI**

**Windows:**
Download from: https://cloud.google.com/sdk/docs/install

**Or use Cloud Shell** (no installation needed):
https://console.cloud.google.com/cloudshell

### **2. Create Google Cloud Project**

```bash
# Login
gcloud auth login

# Create project
gcloud projects create yolov5-app-123 --name="YOLOv5 Web App"

# Set project
gcloud config set project yolov5-app-123

# Enable billing (required)
# Go to: https://console.cloud.google.com/billing
```

### **3. Enable APIs**

```bash
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable containerregistry.googleapis.com
```

### **4. Deploy**

```bash
# Navigate to project folder
cd "C:\Users\pitha\OneDrive\Documents\New Folder\yolov5"

# Deploy
gcloud run deploy yolov5-webapp \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 2Gi \
  --cpu 2 \
  --timeout 300
```

### **5. Get Your URL**

```bash
gcloud run services describe yolov5-webapp --region us-central1 --format 'value(status.url)'
```

---

## 🎯 One-Line Deploy (After Setup)

```bash
gcloud run deploy yolov5-webapp --source . --region us-central1 --allow-unauthenticated --memory 2Gi --cpu 2
```

---

## 💡 Common Commands

```bash
# View logs
gcloud run services logs tail yolov5-webapp --region us-central1

# Update deployment
gcloud run deploy yolov5-webapp --source . --region us-central1

# Delete service
gcloud run services delete yolov5-webapp --region us-central1

# Get URL
gcloud run services describe yolov5-webapp --region us-central1 --format 'value(status.url)'

# List services
gcloud run services list
```

---

## 💰 Cost

**Free Tier:**
- 2 million requests/month
- 360,000 GB-seconds
- 180,000 vCPU-seconds

**After free tier:** ~$0.00012 per request (5 seconds)

**Tip:** Set `--min-instances 0` to save costs (default)

---

## 🔧 Configuration

### **Increase Memory**
```bash
--memory 4Gi
```

### **Increase CPU**
```bash
--cpu 4
```

### **Keep Warm (no cold starts)**
```bash
--min-instances 1
```

### **Different Region**
```bash
--region europe-west1  # Belgium
--region asia-southeast1  # Singapore
```

---

## ✅ Deployment Checklist

- [ ] gcloud CLI installed
- [ ] Logged in (`gcloud auth login`)
- [ ] Project created
- [ ] Billing enabled
- [ ] APIs enabled
- [ ] In project directory
- [ ] Run deploy command
- [ ] Get service URL
- [ ] Test upload mode
- [ ] Test live camera

---

## 🆘 Troubleshooting

### **"gcloud not found"**
Install from: https://cloud.google.com/sdk/docs/install

### **"Billing not enabled"**
Enable at: https://console.cloud.google.com/billing

### **"Build failed"**
Check logs: `gcloud builds list`

### **"Service crashes"**
Increase memory: `--memory 4Gi`

### **"Timeout errors"**
Increase timeout: `--timeout 600`

---

## 📚 Files Created

- ✅ **Dockerfile** - Container config
- ✅ **requirements_deploy.txt** - Dependencies
- ✅ **cloudbuild.yaml** - Build config
- ✅ **.gcloudignore** - Exclude files
- ✅ **deploy.bat** - Windows deploy script
- ✅ **DEPLOYMENT_GUIDE.md** - Full guide
- ✅ **DEPLOY_QUICK_START.md** - This file

---

## 🎉 After Deployment

Your app will be live at:
```
https://yolov5-webapp-xxxxxxxxxx-uc.a.run.app
```

**Features:**
- ✅ HTTPS enabled (required for camera)
- ✅ Auto-scaling (0 to 10 instances)
- ✅ Global CDN
- ✅ 99.95% uptime SLA
- ✅ Automatic SSL certificates

---

## 🚀 Deploy Now!

```bash
gcloud run deploy yolov5-webapp --source . --region us-central1 --allow-unauthenticated --memory 2Gi --cpu 2
```

**Good luck! 🎯**
