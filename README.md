# 🔬 PCOs Detection & Support System Using Deep Learning 

## 🎯 Project Overview

This project implements a Convolutional Neural Network (CNN) model designed to detect Polycystic Ovary Syndrome (PCOS) from ultrasound images. The model has been trained to identify characteristic patterns associated with PCOS, providing a preliminary screening tool for healthcare professionals.

## 📱 Check the Model in Action
You can check the model's predictions for ultrasound images using our Streamlit app:
- [Image Prediction App](https://pcosassistance.streamlit.app/)

## 🧠 Model Architecture

Our CNN model architecture is specifically optimized for analyzing ultrasound imagery:
- Input Layer: Accepts grayscale ultrasound images
- Multiple Convolutional Layers: For feature extraction
- Pooling Layers: For dimensional reduction
- Dense Layers: For final classification
- Output: Binary classification (PCOS positive/negative)

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system
- Git installed
- VS Code (recommended) or any preferred IDE

### Environment Setup
1. **Clone the Repository**
   ```bash
   git clone [repository-url]
   cd [repository-name]
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv pcos_env

   # Activate virtual environment
   # For Windows:
   pcos_env\Scripts\activate
   # For Linux/Mac:
   source pcos_env/bin/activate
   ```

3. **Install Required Packages**
   ```bash
   # Upgrade pip first
   pip install --upgrade pip

   # Option 1: Install from requirements.txt
   pip install -r requirements.txt

   # Option 2: If requirements.txt is not available, install core packages
   pip install numpy pandas matplotlib opencv-python scikit-learn tensorflow keras pillow seaborn ipykernel jupyter
   ```

4. **Setup Jupyter Kernel**
   ```bash
   python -m ipykernel install --user --name=pcos_env
   ```

5. **IDE Setup**
   - **For VS Code Users:**
     1. Open your `.ipynb` file
     2. Click kernel selector (top-right corner)
     3. Select "Python Environments..."
     4. Choose "pcos_env"
   
   - **For Jupyter Notebook Users:**
     1. Run `jupyter notebook` in terminal
     2. Open your notebook
     3. Select Kernel → Change kernel → pcos_env

### Dataset Preparation
1. Download the training and testing datasets
2. Place the datasets in the same directory as the notebook

### Running the Model
1. Open the notebook in your IDE
2. Ensure "pcos_env" kernel is selected
3. Execute all cells sequentially

### Common Setup Issues
- If kernel not showing up: Restart IDE
- If packages missing: Ensure virtual environment is activated (should see `(pcos_env)` in terminal)
- For package conflicts: Create a new virtual environment and reinstall packages

## 📊 Results
- Model Accuracy: [1]
- Validation Results: [0.99]
- Testing Performance: [Ongoing]

## 🎯 Future Vision: PCOs Support System

I am working towards developing a comprehensive support system for women with PCOS. Our vision includes:

### 📱 Mobile Application
- Easy-to-use interface for symptom tracking
- Ultrasound image analysis
- Secure health data storage

### 🍎 Personalized Care
- Custom diet plans based on individual needs
- Activity recommendations
- Integration with gynecologist reports

### 👩‍⚕️ Healthcare Integration
- Direct communication with healthcare providers
- Regular monitoring and feedback
- Automated report generation

## 🤝 Contributing
We welcome contributions! Here's how you can help:
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 🙏 Acknowledgments
- Special thanks to all contributors

## 📞 Contact
- LinkedIn: [[My LinkedIn](https://www.linkedin.com/in/shubham-damai-data-analyst/)]
- Email: [damaishubham14@gmail.com]
- Kaggle: [[My Kaggle](https://www.kaggle.com/shubhamdamai)]

---
**Together, let's make PCOS detection and management more accessible to women worldwide! 💪**


