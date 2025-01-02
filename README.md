---

# **Real-Time Face Recognition Attendance Recorder**

<p align="center">
  <b>A cutting-edge, AI-powered tool that uses facial recognition to automate attendance tracking. This project utilizes advanced machine learning and computer vision techniques to deliver a seamless, real-time attendance recording experience for institutions and organizations.</b>
</p>

---

## 📑 **Table of Contents**

- [Features](#-features)  
- [Installation](#-installation)  
- [Usage](#-usage)  
- [Project Structure](#-project-structure)  
- [Contributing](#-contributing)  
- [License](#-license)  

---

## 🌟 **Features**

- 📷 **Real-Time Face Detection**: Detects faces using advanced computer vision algorithms.  
- 🎯 **Accurate Face Recognition**: Identifies registered faces with high accuracy, leveraging the LBPH (Local Binary Patterns Histograms) algorithm.  
- 📝 **Automated Attendance Recording**: Updates attendance records directly into an Excel file.  
- 📧 **Email Notifications**: Sends attendance summaries to relevant individuals.  
- 🖥️ **User-Friendly GUI**: Easy-to-use interface for adding and managing user profiles and records.  

---

## 🚀 **Installation**

1. Clone the repository:  

   ```bash
   git clone https://github.com/JashanMaan28/Real-Time-FaceRecognition-Attendance-Recorder.git
   ```

2. Navigate to the project directory:  

   ```bash
   cd Real-Time-FaceRecognition-Attendance-Recorder
   ```

3. Install the required dependencies:  

   ```bash
   pip install -r requirements.txt
   ```

4. Ensure the Haar Cascade file for face detection is available:  

   Download the `haarcascade_frontalface_default.xml` file from [OpenCV's repository](https://github.com/opencv/opencv/tree/master/data/haarcascades) and place it in the project directory.  

---

## 🖥️ **Usage**

1. Run the application to add faces first:  

   ```bash
   python add_faces.py 
   ```

2. Add new users:  

   - Use the GUI to capture facial data for each individual and save it to the database.  

3. Start Attendance:  

   - Launch the attendance system to detect and recognize faces in real time. Attendance records will be updated automatically.  

   ```bash
   python main.py 
   ```

4. View Attendance Reports:  

   - Access the Excel files generated in the `/records` directory to view or edit attendance data.  

5. You can use the 'app.py' program to view the records :  

   ```bash
   python app.py 
   ``` 


---

## 🤝 **Contributing**

Contributions are welcome! Here's how you can help:  

1. Fork the repository.  
2. Create a feature branch:  

   ```bash
   git checkout -b feature/YourFeature
   ```

3. Commit your changes:  

   ```bash
   git commit -m "Add YourFeature"
   ```

4. Push the branch:  

   ```bash
   git push origin feature/YourFeature
   ```

5. Open a Pull Request.  

---

## 📄 **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.  

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/JashanMaan28">Jashanpreet Singh</a>
</p>  

---  
