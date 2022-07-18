from django.db import connections


def call_stored_function(function_name, db_name='default', single=False, *args):
    """
    function_name: str - stored function name with schema EX: public.some_function
    """
    try:
        with connections[db_name].cursor() as cursor:
            result = []
            # Выполняем функцию на базе
            cursor.callproc(function_name, args)

            
            # Получем описание возвращаемого значения
            desc = cursor.description
            row_count = cursor.rowcount
 
            if(row_count):
                result = [
                    dict(zip([col.name for col in desc], row))
                    for row in cursor.fetchmany(row_count)
                ]
 
            if single:
                if len(result):
                    return result[0]
 
            return result
    except Exception as e:
        raise e
 
 
def call_stored_procedure(proc_name, db_name="default", *args):
    try:
        with connections[db_name].cursor() as cursor:
            result = {}
            i = 0
            while len(args) > i:
                result[i] = "%s"
                i = i + 1
            proc_param = ",".join(str(key) for key in result.values())
            cursor.execute("call "+proc_name+"("+proc_param+")", args)
 
            desc = cursor.description
 
            # 
            if not desc:
                result = {'p_result': 0, 'p_resultmessage': ''}
            else:
                result = dict(zip([col.name for col in desc], cursor.fetchone()))
 
            return result
    except Exception as e:
        raise(e)
