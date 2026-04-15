import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


# -----------------------------
# Digital Signature Setup
# -----------------------------
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()


# -----------------------------
# Vehicle Registration Storage
# -----------------------------
vehicles = {}


# -----------------------------
# SHA-256 Hash Function
# -----------------------------
def generate_hash():
    message = input("Enter message to hash: ")
    sha_hash = hashlib.sha256(message.encode()).hexdigest()
    print("\nSHA-256 Hash:")
    print(sha_hash)


# -----------------------------
# Digital Signature Function
# -----------------------------
def sign_message():
    message = input("Enter message to sign: ")

    signature = private_key.sign(
        message.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    print("\nMessage signed successfully.")
    print("Signature (hex):")
    print(signature.hex())

    return message, signature


# -----------------------------
# Signature Verification
# -----------------------------
def verify_signature():
    message = input("Enter original message: ")
    signature_hex = input("Enter signature (hex): ")

    try:
        signature = bytes.fromhex(signature_hex)

        public_key.verify(
            signature,
            message.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )

        print("Signature is VALID.")

    except Exception:
        print("Signature is INVALID.")


# -----------------------------
# Register Vehicle
# -----------------------------
def register_vehicle():
    plate = input("Enter Number Plate: ").upper()

    if plate in vehicles:
        print("Vehicle already registered.")
        return

    owner = input("Enter Owner Name: ")
    model = input("Enter Vehicle Model: ")

    vehicles[plate] = {
        "owner": owner,
        "model": model
    }

    print("Vehicle registered successfully.")


# -----------------------------
# Retrieve Vehicle
# -----------------------------
def get_vehicle():
    plate = input("Enter Number Plate: ").upper()

    if plate not in vehicles:
        print("Vehicle not found.")
        return

    print("\nVehicle Details:")
    print(f"Owner: {vehicles[plate]['owner']}")
    print(f"Model: {vehicles[plate]['model']}")


# -----------------------------
# Main Menu
# -----------------------------
def main():
    while True:
        print("\n===== Cryptography and Vehicle Registration System =====")
        print("1. Generate SHA-256 Hash")
        print("2. Create Digital Signature")
        print("3. Verify Digital Signature")
        print("4. Register Vehicle")
        print("5. Retrieve Vehicle")
        print("6. Exit")

        choice = input("Enter your choice: ")

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
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
