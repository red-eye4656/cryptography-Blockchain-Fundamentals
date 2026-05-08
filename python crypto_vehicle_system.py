import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PrivateFormat,
    NoEncryption,
    PublicFormat
)

# ==============================
# Vehicle Registration Database
# ==============================
vehicles = {}

# ==============================
# Generate RSA Key Pair
# ==============================
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

# ==============================
# SHA-256 Hashing Function
# ==============================
def generate_hash():
    message = input("Enter message to hash: ")

    sha256_hash = hashlib.sha256(message.encode()).hexdigest()

    print("\nSHA-256 Hash:")
    print(sha256_hash)


# ==============================
# Digital Signature Functions
# ==============================
def sign_message():
    message = input("Enter message to sign: ")

    signature = private_key.sign(
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("\nMessage Signed Successfully!")
    print("Signature (hex):")
    print(signature.hex())

    return message, signature


def verify_signature():
    message = input("Enter original message: ")
    signature_hex = input("Enter signature (hex): ")

    try:
        signature = bytes.fromhex(signature_hex)

        public_key.verify(
            signature,
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        print("\n✅ Signature is VALID")

    except Exception:
        print("\n❌ Signature is INVALID")


# ==============================
# Vehicle Registration Functions
# ==============================
def register_vehicle():
    number_plate = input("Enter Number Plate: ").upper()

    # Check duplicate number plate
    if number_plate in vehicles:
        print("\n❌ Vehicle with this Number Plate already exists.")
        return

    owner = input("Enter Owner Name: ")
    model = input("Enter Vehicle Model: ")

    vehicles[number_plate] = {
        "owner": owner,
        "model": model
    }

    print("\n✅ Vehicle Registered Successfully!")


def get_vehicle():
    number_plate = input("Enter Number Plate to search: ").upper()

    if number_plate in vehicles:
        vehicle = vehicles[number_plate]

        print("\nVehicle Details")
        print("-------------------")
        print(f"Owner : {vehicle['owner']}")
        print(f"Model : {vehicle['model']}")

    else:
        print("\n❌ Vehicle not found.")


# ==============================
# Main Menu
# ==============================
def main():
    while True:
        print("\n========== MENU ==========")
        print("1. Generate SHA-256 Hash")
        print("2. Sign Message")
        print("3. Verify Digital Signature")
        print("4. Register Vehicle")
        print("5. Retrieve Vehicle Details")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            generate_hash()

        elif choice == "2":
            sign_message()

        elif choice == "3":
            verify_signature()

        elif choice == "4":
            register_vehicle()

        elif choice == "5":
            get_vehicle()

        elif choice == "6":
            print("\nExiting Program...")
            break

        else:
            print("\n❌ Invalid choice. Try again.")


# Run Program
if __name__ == "__main__":
    main()
