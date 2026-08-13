[streamlit]

# Streamlit configuration for deployment

# Set theme
theme.base="light"
theme.primaryColor="#FF6B6B"
theme.backgroundColor="#FFFFFF"
theme.secondaryBackgroundColor="#F0F2F6"
theme.textColor="#262730"
theme.font="sans serif"

# Set page layout
client.layoutMode="centered"
client.maxUploadSize=200

# Server settings
server.port=8501
server.headless=true
server.enableXsrfProtection=true
server.enableCORS=true

# Logger settings
logger.level="info"
