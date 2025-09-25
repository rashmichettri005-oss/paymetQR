import qrcode

# Taking inputs from the user
upi_id = input("Enter your UPI ID: ")
recipient_name = input("Enter Recipient Name: ")
amount = input("Enter Amount (INR): ")

# Base UPI payment URL format
# upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=INR

# Defining the payment URLs for each app
phonepe_url = f'upi://pay?pa={upi_id}&pn={recipient_name}&am={amount}&cu=INR'
paytm_url = f'upi://pay?pa={upi_id}&pn={recipient_name}&am={amount}&cu=INR'
google_pay_url = f'upi://pay?pa={upi_id}&pn={recipient_name}&am={amount}&cu=INR'

# Create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save the QR code images (optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# Display the QR codes
print("QR Codes generated! They should open now...")
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
