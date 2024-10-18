
import sqlite3
from groq import Groq

# Initialize Groq client
api_key = "Your Api Key"  
groq_client = Groq(api_key=api_key)

def fetch_db_schema():
    return """
    Table: artists
    Columns:
    - Artist_ID (int, primary key)
    - Artist_Name (text)
    - Genre (text)
    - Email (text)

    Table: venues
    Columns:
    - Venue_ID (int, primary key)
    - Venue_Name (text)
    - Location (text)
    - Capacity (int)

    Table: concerts
    Columns:
    - Concert_ID (int, primary key)
    - Artist_ID (int, foreign key references artists(Artist_ID))
    - Venue_ID (int, foreign key references venues(Venue_ID))
    - Concert_Date (text)
    - Ticket_Price (real)
    - Tickets_Available (int)

    Table: customers
    Columns:
    - Customer_ID (int, primary key)
    - Customer_Name (text)
    - Customer_Country (text)
    - Email (text)
    - Date_Of_Birth (text)

    Table: tickets
    Columns:
    - Ticket_ID (int, primary key)
    - Concert_ID (int, foreign key references concerts(Concert_ID))
    - Customer_ID (int, foreign key references customers(Customer_ID))
    - Purchase_Date (text)
    - Quantity (int)
    - Payment_Method (text)
    """

def convert_question_to_sql(user_question):
    schema = fetch_db_schema()
    
    prompt = f"""
    Given the following database schema:

    {schema}

    Generate a SQL query to answer the following question:
    {user_question}

    Provide only the SQL query without any additional explanation.
    """

    response = groq_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.1-8b-instant",
        max_tokens=300,
        temperature=0.2,
    )

    sql_query_result = response.choices[0].message.content.strip()
    
# Clean the SQL query
    if sql_query_result.startswith('```sql'):
        sql_query_result = sql_query_result[6:].strip()  
    if sql_query_result.endswith('```'):
        sql_query_result = sql_query_result[:-3].strip()  

    return sql_query_result

def run_sql_query(sql_query_result):
    connection = sqlite3.connect('concerts_tickets_database.db') 
    db_cursor = connection.cursor()
    db_cursor.execute(sql_query_result)
    query_output = db_cursor.fetchall()
    connection.close()
    return query_output

def derive_insight(user_question, sql_query_result, query_output):
    schema = fetch_db_schema()
    
    prompt = f"""
    Context:
    - User Question: {user_question}
    - SQL Query: {sql_query_result}
    - Query Results: {query_output}
    - Database Schema: {schema}

    Task: Based on the query results, provide a clear and concise insight directly answering the user's question. Only use the provided query result data, without introducing additional information.

    Insight:
    """

    response = groq_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.1-8b-instant",
        max_tokens=200,
        temperature=0.5,
    )

    return response.choices[0].message.content

def process_user_input():
    while True:
        user_question = input("Ask a question about our concert or ticket data (or type 'quit' to exit): ")
        if user_question.lower() == 'quit':
            print("Thank you! Have a great day!")
            break

        
        sql_query_result = convert_question_to_sql(user_question)
        print(f"Generated SQL Query: {sql_query_result}")
        
        try:
            query_output = run_sql_query(sql_query_result)
            print("Query Results:")
            for row in query_output:
                print(row)
            
            insight = derive_insight(user_question, sql_query_result, query_output)
            print("\nInsight:")
            print(insight)
        except sqlite3.Error as error_msg:
            print(f"An error occurred: {error_msg}")

if __name__ == "__main__":
    process_user_input()














