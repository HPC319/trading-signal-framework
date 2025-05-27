from jwt_auth import create_coinbase_jwt

def main():
    jwt_token = create_coinbase_jwt()
    print("✅ JWT Created Successfully")
    print(jwt_token)

if __name__ == "__main__":
    main()
