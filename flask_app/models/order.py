from flask_app.config.mysqlconnection import connectToMySQL

class Order:
    def __init__(self,data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.number_of_boxes = data['number_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_one(cls,data):
        query = '''
                SELECT * FROM orders WHERE id = %(order_id)s;
                '''
        results = connectToMySQL('cookie_orders').query_db(query,data)
        order = cls(results[0])
        return order

    @classmethod
    def get_all(cls):
        query = '''
                SELECT * FROM orders;
                '''
        results = connectToMySQL('cookie_orders').query_db(query)
        orders = []
        for row in results:
            orders.append(cls(row))
        return orders
        
    @classmethod
    def save(cls,data):
        query = '''
                INSERT INTO orders (customer_name,cookie_type,number_of_boxes)
                VALUES (%(customer_name)s,%(cookie_type)s,%(number_of_boxes)s);
                '''
        return connectToMySQL('cookie_orders').query_db(query,data)
        
    @classmethod
    def update(cls,data):
        query = '''
                UPDATE orders
                SET customer_name=%(customer_name)s,
                    cookie_type=%(cookie_type)s,
                    number_of_boxes=%(number_of_boxes)s;
                WHERE id=%(order_id)s;
                '''
        return connectToMySQL('cookie_orders').query_db(query,data)
        
    @classmethod
    def delete(cls,data):
        query = '''
                DELETE FROM orders WHERE id=%(order_id)s;
                '''
        return connectToMySQL('cookie_orders').query_db(query,data)
        
    # @classmethod
    # def xxx(cls,data):
    #     pass


