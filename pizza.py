from flask import Flask, request, jsonify
import MysqlConnect as connect
import GenerateResponse as res
import Error as err

app = Flask(__name__)


@app.route('/insert', methods=['get', 'post'])
def insert():
    req = request.json
    pizza_size = req['conversation']['memory']['pizza_size']['value']
    pizza_type = req['conversation']['memory']['pizza_type']['value']
    number = str(req['conversation']['memory']['number']['scalar'])
    pizza_variety = req['conversation']['memory']['pizza_variety']['value']
    id = "123"


    conn = connect.ConnectMySql()
    print(f'Connection status : {conn}')
    if (conn is False):
        return err.ReturnConnectionError()
    else:
        try:
            cur1 = conn.cursor()
            query = (f"INSERT INTO  details (Number,Type,Size,Id) VALUES ('{number}','{pizza_type}','{pizza_size}','{id}')")
            print(query)
            cur1.execute(query)
            conn.commit()
            msg = "Data inserted succesfully"
            cur2 = conn.cursor()
            query = ('Select * from details')
            cur2.execute(query)
            for i in cur2:
                id = i[3]

            return jsonify({
                "replies": [
                    {
                        "type": "text",
                        "content": "Ordered successfully...\nYour Order Id is " + str(id) +"."
                    }
                ]
            }
            )
        except Exception as e:
            print(e)
            return err.ReturnFetchError()
        finally:
            conn.close()


if __name__ == '__main__':
    app.run(debug=True, port=3000)
