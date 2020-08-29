import apps

def save_app_state_variable_with_dialog(app_name, var_name, var_value):
    # print("save_app_state_variable_with_dialog(%s, %s, %s)" % (app_name, var_name, str(var_value)))
    apps.save_app_state_variable(app_name, var_name, var_value)
    return
