import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
from io import BytesIO

# Set page configuration
st.set_page_config(
    page_title="PCOS Detection",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS to control width and styling
st.markdown("""
    <style>
        .main > div {
            max-width: 1200px;
            padding: 1rem;
        }
        .stImage {
            max-width: 470px !important;
            margin: auto;
        }
        .css-1v0mbdj.e115fcil1 {
            max-width: 1200px;
            margin: auto;
        }
        .image-container {
            background-color: #ffffff;
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: auto;
            max-width: 470px;
        }
    </style>
""", unsafe_allow_html=True)

# Load the model
@st.cache_resource
def load_model():
    try:
        model = tf.keras.models.load_model('pcos_detection_model.h5')
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def preprocess_image(image, target_size=(224, 224)):
    """
    Preprocess the uploaded image for model prediction
    """
    # Convert to grayscale if the image is RGB
    if image.mode != 'L':  # If not already grayscale
        image = image.convert('L')
        # Convert back to RGB (3 channels) as model expects RGB input
        image = Image.merge('RGB', (image, image, image))
    
    # Resize image
    image = image.resize(target_size)
    
    # Convert to numpy array and normalize
    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    
    return img_array

def predict_pcos(model, image_array):
    """
    Make prediction using the model
    """
    try:
        prediction = model.predict(image_array)
        probability = prediction[0][0]
        result = 'PCOS Negative' if probability > 0.5 else 'PCOS Positive'
        return result, probability
    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")
        return None, None

def main():
    # Sidebar
    st.sidebar.title("Upload Image")
    st.sidebar.write("Upload an ultrasound image to check for PCOS")
    
    # File uploader in sidebar
    uploaded_file = st.sidebar.file_uploader(
        "Choose an ultrasound image...", 
        type=["jpg", "jpeg", "png"],
        help="Upload an ultrasound image (max 10MB)",
        accept_multiple_files=False
    )
    
    # Check button in sidebar
    check_button = st.sidebar.button("Check for PCOS", use_container_width=True)
    
    # Add disclaimer in sidebar
    st.sidebar.markdown("---")
    st.sidebar.info("""
    Please note: This is an AI-based prediction and should not be used as a definitive 
    medical diagnosis. Always consult with a healthcare professional for proper diagnosis 
    and treatment.
    """)
    
    # Main content area
    st.title("PCOS Detection from Ultrasound Images")
    
    # Load model
    model = load_model()
    
    if model is None:
        st.error("Failed to load model. Please check if the model file exists.")
        return
    
    # Main content layout
    if uploaded_file is not None:
        # Check file size
        if uploaded_file.size > 10 * 1024 * 1024:  # 10MB limit
            st.error("File size exceeds 10MB limit. Please upload a smaller file.")
            return
            
        try:
            # Display the image in Instagram-like container
            image = Image.open(uploaded_file)
            
            # Create centered columns for the image
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.markdown('<div class="image-container">', unsafe_allow_html=True)
                st.image(image, caption="Uploaded Image", use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            # Make prediction when button is clicked
            if check_button:
                with st.spinner("Analyzing image..."):
                    # Preprocess image
                    processed_image = preprocess_image(image)
                    
                    # Make prediction
                    result, probability = predict_pcos(model, processed_image)
                    
                    if result:
                        # Create columns for centered result
                        col1, col2, col3 = st.columns([1, 2, 1])
                        with col2:
                            # Display result with custom styling
                            result_color = "red" if "Positive" in result else "green"
                            st.markdown(f"""
                                <div style='text-align: center; padding: 2rem; background-color: #f0f2f6; border-radius: 10px;'>
                                    <h2 style='color: {result_color};'>{result}</h2>
                                    <p>Confidence: {abs(probability - 0.5) * 2:.2%}</p>
                                </div>
                            """, unsafe_allow_html=True)
        
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")
            st.write("Please ensure you've uploaded a valid image file.")
    else:
        # Display placeholder when no image is uploaded
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
                <div style='text-align: center; padding: 2rem; background-color: #f0f2f6; border-radius: 10px;'>
                    <p>Please upload an ultrasound image using the sidebar to begin analysis.</p>
                </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()