// YOLOv5 Object Detection Web App - JavaScript

let currentResultUrl = "";

// Initialize
document.addEventListener("DOMContentLoaded", function () {
  const uploadBox = document.getElementById("uploadBox");
  const fileInput = document.getElementById("fileInput");

  // Click to upload
  uploadBox.addEventListener("click", () => fileInput.click());

  // File input change
  fileInput.addEventListener("change", handleFileSelect);

  // Drag and drop
  uploadBox.addEventListener("dragover", handleDragOver);
  uploadBox.addEventListener("dragleave", handleDragLeave);
  uploadBox.addEventListener("drop", handleDrop);
});

function handleDragOver(e) {
  e.preventDefault();
  e.stopPropagation();
  document.getElementById("uploadBox").classList.add("dragover");
}

function handleDragLeave(e) {
  e.preventDefault();
  e.stopPropagation();
  document.getElementById("uploadBox").classList.remove("dragover");
}

function handleDrop(e) {
  e.preventDefault();
  e.stopPropagation();
  document.getElementById("uploadBox").classList.remove("dragover");

  const files = e.dataTransfer.files;
  if (files.length > 0) {
    uploadFile(files[0]);
  }
}

function handleFileSelect(e) {
  const files = e.target.files;
  if (files.length > 0) {
    uploadFile(files[0]);
  }
}

function uploadFile(file) {
  // Validate file
  const allowedTypes = [
    "image/jpeg",
    "image/png",
    "image/gif",
    "image/bmp",
    "video/mp4",
    "video/avi",
    "video/quicktime",
    "video/x-matroska",
  ];

  if (!allowedTypes.includes(file.type)) {
    alert("Invalid file type. Please upload an image or video file.");
    return;
  }

  if (file.size > 100 * 1024 * 1024) {
    alert("File too large. Maximum size is 100MB.");
    return;
  }

  // Show progress
  document.getElementById("uploadBox").style.display = "none";
  document.getElementById("progressContainer").style.display = "block";
  document.getElementById("resultsSection").style.display = "none";

  const progressFill = document.getElementById("progressFill");
  const progressText = document.getElementById("progressText");

  progressFill.style.width = "0%";
  progressText.textContent = "Uploading...";

  // Create form data
  const formData = new FormData();
  formData.append("file", file);

  // Upload with progress
  const xhr = new XMLHttpRequest();

  xhr.upload.addEventListener("progress", (e) => {
    if (e.lengthComputable) {
      const percentComplete = (e.loaded / e.total) * 50; // 50% for upload
      progressFill.style.width = percentComplete + "%";
    }
  });

  xhr.addEventListener("load", () => {
    if (xhr.status === 200) {
      progressFill.style.width = "50%";
      progressText.textContent = "Processing with YOLOv5...";

      const response = JSON.parse(xhr.responseText);

      // Simulate processing progress
      let progress = 50;
      const interval = setInterval(() => {
        progress += 5;
        if (progress >= 100) {
          clearInterval(interval);
          progressFill.style.width = "100%";
          progressText.textContent = "Complete!";

          setTimeout(() => {
            displayResults(response);
          }, 500);
        } else {
          progressFill.style.width = progress + "%";
        }
      }, 200);
    } else {
      const error = JSON.parse(xhr.responseText);
      alert("Error: " + (error.error || "Upload failed"));
      resetUpload();
    }
  });

  xhr.addEventListener("error", () => {
    alert("Upload failed. Please try again.");
    resetUpload();
  });

  xhr.open("POST", "/upload");
  xhr.send(formData);
}

function displayResults(response) {
  document.getElementById("progressContainer").style.display = "none";
  document.getElementById("resultsSection").style.display = "block";

  currentResultUrl = response.result_url;
  const data = response.data;

  // Display statistics
  const statsGrid = document.getElementById("statsGrid");
  statsGrid.innerHTML = "";

  if (response.type === "image") {
    statsGrid.innerHTML = `
            <div class="stat-card">
                <div class="stat-value">${data.total_objects}</div>
                <div class="stat-label">Objects Detected</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">${Object.keys(data.object_counts).length}</div>
                <div class="stat-label">Unique Classes</div>
            </div>
        `;
  } else {
    statsGrid.innerHTML = `
            <div class="stat-card">
                <div class="stat-value">${data.processed_frames}</div>
                <div class="stat-label">Frames Processed</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">${data.fps}</div>
                <div class="stat-label">FPS</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">${data.total_detections}</div>
                <div class="stat-label">Total Detections</div>
            </div>
        `;
  }

  // Display media
  const resultMedia = document.getElementById("resultMedia");
  if (response.type === "image") {
    resultMedia.innerHTML = `<img src="${response.result_url}" alt="Detection Result">`;
  } else {
    resultMedia.innerHTML = `
            <video controls>
                <source src="${response.result_url}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        `;
  }

  // Display detection details
  const detectionDetails = document.getElementById("detectionDetails");
  if (Object.keys(data.object_counts).length > 0) {
    let objectListHTML = '<h3>Detected Objects</h3><div class="object-list">';

    // Sort by count (descending)
    const sortedObjects = Object.entries(data.object_counts).sort(
      (a, b) => b[1] - a[1],
    );

    sortedObjects.forEach(([name, count], index) => {
      objectListHTML += `
                <div class="object-item" style="--item-index: ${index}">
                    <span class="object-name">${name}</span>
                    <span class="object-count">${count}</span>
                </div>
            `;
    });

    objectListHTML += "</div>";
    detectionDetails.innerHTML = objectListHTML;
  } else {
    detectionDetails.innerHTML = "<h3>No objects detected</h3>";
  }

  // Scroll to results
  document
    .getElementById("resultsSection")
    .scrollIntoView({ behavior: "smooth" });
}

function resetUpload() {
  document.getElementById("uploadBox").style.display = "block";
  document.getElementById("progressContainer").style.display = "none";
  document.getElementById("resultsSection").style.display = "none";
  document.getElementById("fileInput").value = "";
  currentResultUrl = "";
}

function downloadResult() {
  if (currentResultUrl) {
    const link = document.createElement("a");
    link.href = currentResultUrl;
    link.download = currentResultUrl.split("/").pop();
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }
}
