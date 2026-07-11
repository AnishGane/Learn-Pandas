1. Run this for creating and activating the `venv` in your project:

   ```
   python -m venv .venv

   .venv\Scripts\activate
   ```

2. Then install the packages needed for your project like pip install pandas numpy seaborn, etc.
3. Generate a `requirements.txt` file with: **pip freeze > requirements.txt**
   - `requirements.txt` is created to save a list of all the python packages with their exact versions that you have installed in your environment.
   - **How does it work?**:
     - **Install the packages**: for e.g.: pip install numpy pandas flask
     - **Save them**: pip freeze > requirements.txt
     - **Share your project**:

     ```
      MyProject/
         │
         ├── app.py
         ├── requirements.txt
         └── README.md
     ```

     - **Someone clones your project**: Instead of installing each package manually, they simply run: `pip install -r requirements.txt`
