from fastapi import FastAPI, HTTPException, Path
from src.connection import connection_url, create_engine, text
from fastapi import Body
from src.basemodels import USER_Model, UserInfoResponse
app = FastAPI(title='Sample API')

@app.get('/get_user_info', status_code=200, response_model=UserInfoResponse,tags=['User Metadata'])
def get_user_info(limits:int =1):
    if limits!=None:
        engine = create_engine(connection_url)
        with engine.connect() as conn:
            query_info = conn.execute(text(" SELECT * FROM  user_info"))
            query_response = query_info.fetchall()

            transform_info = [USER_Model(user_name = row[0],
                                         age       = row[1],
                                         experience= row[2],
                                         user_id   = row[3]).model_dump() for row in query_response]
            
            # print(transform_info)
            return {"user_info":transform_info[:limits]}
    else:
        raise  HTTPException(status_code = 404,
                             detail      = "Connection Fail") 
    

@app.post('/insert_user_info', status_code=200,tags=['User Metadata'])
def post_user_info(insert_info: UserInfoResponse = Body(...)):

    if insert_info is not None:
        
        transform_info = [row.model_dump() for records in insert_info for row in records[1] if row.model_dump()['user_id']!=0]
        
        if len(transform_info)!=0:
            engine = create_engine(connection_url)

            insertion_query = text(""" 
                                SET IDENTITY_INSERT user_info ON;
                                INSERT INTO user_info (user_name, age, experience, user_id) 
                                VALUES (:user_name, :age, :experience, :user_id)
                                SET IDENTITY_INSERT user_info OFF;
                                """)    
            counter = 0
            with engine.connect() as conn:
                for insert_parameter in transform_info:
                    try:
                        conn.execute(insertion_query,[insert_parameter])
                        conn.commit() 
                        counter+=1
                    except: 
                        print("Insertion Fail beacuase of duplicate Records")

            return {"response":f"Total Number of Record Inserted is :{counter}"}
        
        else:
            return {"response":"Insert Unique Records"}
        
    else:
        raise HTTPException(status_code=404, detail="Request Fail")

@app.put("/update_user_info/{user_id}", status_code=200, tags=["User Metadata"])
def update_user_info(
    user_id: int = Path(..., title="The ID of the user to update"),
    user_data: USER_Model = ...,):
    
    if user_id is not None:
        engine = create_engine(connection_url)

        query_info = text(f"SELECT * FROM user_info WHERE user_id={user_id}")
        
        # print([user_data])
        with engine.connect() as conn:
            check_query_info = conn.execute(query_info)
            query_response   = check_query_info.fetchall()

            transform_info = [USER_Model(user_name = row[0],
                                         age       = row[1],
                                         experience= row[2],
                                         user_id   = row[3]).model_dump() for row in query_response]
            
            if len(transform_info)!=0:
                update_parameters = [row.model_dump() for row in [user_data]]
                update_query = text("""
                                        UPDATE user_info 
                                        SET user_name = :user_name, age = :age, experience = :experience 
                                        WHERE user_id = :user_id
                                    """)
                
                conn.execute(update_query,update_parameters)
                conn.commit() 

                return {"response":f"{user_id} updated with latest info","metadata":update_parameters}
            
            else:
                return {"response":f"{user_id} does not Exist"}
 
    else:
        raise HTTPException(status_code=404, detail="Request Fail")
    
@app.delete("/delete_user_info/{user_id}", status_code=200, tags=["User Metadata"])
def delete_user_info(user_id: int = Path(..., title="The ID of the user to update")):
    if user_id is not None:
        engine = create_engine(connection_url)

        delete_query = text(f"DELETE user_info WHERE user_id={user_id}")
        with engine.connect() as conn:
            try:
                conn.execute(delete_query)
                conn.commit()
                return {"response":f"{user_id} user_id deleted info the table"}
            except:
                   return {"response":f"{user_id} user_id does not exist"}
            
    else:
        raise HTTPException(status_code=404, detail="Request Fail")