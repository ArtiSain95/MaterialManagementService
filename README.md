# Backend Developer Challenge

## Objective:

Create a REST API to manage chemical materials.

1. **Create Material**: Implement a POST route /material that accepts JSON payloads like:

```json
{
  "formula": "CO2",
  "density": 1.87
}
```

Save the material and return its unique ID.

2. **Retrieve Material**: Implement a GET route /material/{id} to fetch a material by its ID.
3. **Search Materials**: Implement a GET route /search with optional filters for:
    - Minimal density
    - Maximal density
    - elements that must be included (e.g. ["H", "O"])
    - elements that must be excluded (e.g. ["Fe"])
4. **Dockerize the API**: Provide a Dockerfile and necessary scripts to run your API in a Docker container.
5. **Advanced Material Properties**: Lets assume we have a function `fooness(formula) -> float` that calculates a 
   property for a given material. We don't know how long this function needs to execute since it is highly depended 
   on the formula. Create a POC for providing functionality (backend only) to a customer to calculate this property for a given 
   material. (You can mock the function `fooness(formula) -> float` to sleep for a random time)

the folder /sample-frontend contains a simple frontend that you can use for reference (but it is not needed)

## Steps(For localhost):

Follow these steps to set up and run the API on your local machine:

1. **Create virtual environment**:
    ```sh
    python3 -m venv .venv
    ```
2. **Activate the virtual env**:
    ```sh
    source .venv/bin/activate
    ```
3. **Install Requirements.txt**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Check for migrations**:
    ```sh
    python3 manage.py makemigrations
    ```
5. **Migrate the database**:
    ```sh
    python3 manage.py migrate
    ```
6. **Run the server**:
    ```sh
    python3 manage.py runserver
    ```

## Steps(For Docker):

1. **Install Docker and Docker compose**:
    - [link](https://docs.docker.com/compose/install/) - Docker installation guide
2. **Build Docker Image and deploy image**:
    ```sh
    docker-compose up -d --build
    ```

## Check on UI:
1. **Navigate to the Homepage**:
   - [Homepage](http://localhost:8000/api/home/) - Visit this link to access the homepage.

2. **Create a New Material**:
   - Enter the Formula and Density in the provided fields under "Create Material."
   - Click the "Create" button.
   - The new material will be added to the database.

3. **Fetch a Material**:
   - Provide the Material ID for the specific material you are looking for.
   - Click the "Get Material" button.
   - The data for the requested material will be displayed if it exists.

4. **Search Materials**:
   - Specify the minimum density to filter materials with densities above the specified value.
   - Specify the maximum density to filter materials with densities below the specified value.
   - Enter elements to include in a comma-separated string in the "Include Elements" input field. This will filter materials containing the specified elements.
   - Enter elements to exclude in a comma-separated string in the "Exclude Elements" input field. This will filter out materials containing the specified elements.

# APIs:

## 1. Fetch Material by ID:

- **Endpoint:** localhost:8000/api/materials/<m_id>/
- **HTTP Method:** GET
- **Payload:** m_id = int
- **Response:** ```{"id":1,"formula":"CO3","density":12.3} ```
- **Description:** Implemented a GET route /material/{id} to retrieve material details by its ID.

## 2. Create Material:

- **Endpoint:** localhost:8000/api/materials/
- **HTTP Method:** POST
- **Payload:** {"formula":"CO3","density":12.3}
- **Response:** ```{"id":1,"formula":"CO3","density":12.3} ```
- **Description:** Implemented a POST route /material/ to create a new material.

## 3. Search Materials:

- **Endpoint:** localhost:8000/api/search/min-density=1&max-density=10&exclude-elements=H&&exclude-elements=H&
- **HTTP Method:** GET
- **Payload:** min-density=1&max-density=10&exclude-elements=H&
- **Response:** ```[{"id":1,"formula":"CO3","density":12.3}] ```
- **Description:** Implemented a GET route /search with optional filters for minimal density, maximal density, included elements, and excluded elements.

## 4. Home:

- **Endpoint:** localhost:8000/api/material/home/
- **HTTP Method:** GET
- **Payload:** 
- **Response:** <raw html>
- **Description:** used the provided sample template.

## 5. Advanced Property Calculation:

- **Endpoint:** localhost:8000/api/material/<int:id>/advanced-property/
- **HTTP Method:** GET
- **Payload:** id = 1
- **Response:** ```{"property_value": <density_value>} ```
- **Description:** Created a POC for backend functionality to calculate advanced properties for a given material.

# POC

This Proof of Concept (POC) demonstrates backend functionality, integrating the `fooness` function for property calculations. The backend-only solution enables customers to retrieve property information for a specified material. A new endpoint, /calculate-property, has been established to handle property calculation requests.

When the API is accessed, it takes the material ID as input. On the backend, this ID is received as input, and the corresponding material record is retrieved. The `fooness` method is then invoked, passing the molecular formula of the material. The `fooness` method returns the property value, which, in this case, is the density of the material.

This POC showcases the seamless integration of backend logic for material property calculations, enhancing the overall functionality of the API.
