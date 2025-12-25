Smart Agriculture Health Monitoring System
The Smart Agriculture Health Monitoring System is a cloud-integrated web application designed to help farmers and researchers identify crop diseases in real-time. By leveraging Artificial Intelligence and Computer Vision, the system analyzes uploaded images of crops to detect specific health issues, ensuring timely intervention and better crop yields.

🌟 Key Features
AI Image Classification: Detects Healthy, Pest Infected, Fungal, Bacterial, and Viral diseases .
Real-time Probability: Provides instant feedback with probability percentages for each diagnosis .
Dynamic Dashboard: The UI uses color-coded cards (Green, Yellow, Purple, Blue, Red) to represent different health statuses .
Cloud Integration: Utilizes Azure Blob Storage for image handling and Azure Custom Vision for high-performance analysis .

⚙️ Technical Stack
Frontend: HTML5, CSS3 (Dynamic Gradients), JavaScript .
Backend: Python Flask .
Cloud Infrastructure: Microsoft Azure (Blob Storage & Custom Vision API) .

🏗️ System Design
This project followed a rigorous engineering process. Detailed diagrams are available in the /docs folder:
Activity Diagram: Outlines the user-to-cloud process flow.
Sequence Diagram: Details the API interaction between Flask and Azure services.
Use Case Diagram: Defines system interactions for agricultural monitoring.

📂 Project Structure
app.py: The Flask server that interfaces with Azure .
index.html: The user interface for uploading and viewing results .
requirements.txt: Python dependencies (Flask, Requests, Azure-Storage-Blob).
/docs: Project report and system architecture diagrams .

⚠️ Note on Cloud Deployment
This project is fully integrated with Azure Blob Storage and Custom Vision AI. To avoid ongoing cloud maintenance costs, the live Azure endpoints are currently paused. However, the full implementation logic for storage and AI inference  is available in app.py for review. To run this locally, please replace the placeholders in app.py with your own Azure credentials.

🎓 Academic Credits
Developer: Kritika Baghel.
Degree: Bachelor of Technology in Computer Science & Technology.
Institution: Manav Rachna University, Faridabad.


Supervisor: Mr. Anup Singh Kushwaha (Assistant Professor).
