To run in local
    docker compose up --build > output.txt

For Render deployment:

Set Build Command: npm ci
Set Start Command: npm start
Add environment variables in Render dashboard


Curl scripts for testing


2. Get (or create) cart

curl -X GET http://localhost:8084/cart \
  -b cookies.txt



3. Add item

curl -X POST http://localhost:8084/cart/items \
  -H "Content-Type: application/json" \
  -b cookies.txt \
  -d '{
    "product_id": 1,
    "quantity": 2,
    "price_at_add": 1000.00
  }'



5. Update item quantity

curl -X PUT http://localhost:8084/cart/items/1 \
  -H "Content-Type: application/json" \
  -b cookies.txt \
  -d '{
    "quantity": 5
  }'



6. Get total

curl -X GET http://localhost:8084/cart/total \
  -b cookies.txt



7. Delete item

curl -X DELETE http://localhost:8084/cart/items/1 \
  -b cookies.txt



8. Admin-only: get all carts

curl -X GET http://localhost:8084/admin/carts \
  -b cookies.txt