import route_encode
import route_decode
def start_route():
    print("\n--- Route Transposition ---")
    msg = input("Shkruaj tekstin: ")
    encoded = route_encode.encrypt(msg)
    print("I Enkriptuar:", encoded)
    print("I Dekriptuar:", route_decode.decrypt(encoded))

if __name__ == "__main__":
    start_route()