from config import Scope

# TODO: Скорее всего есть более хороший способ реализовать это.
actual_scope_names = {
    Scope.personal: "GIGACHAT_API_PERS",
    Scope.b2b: "GIGACHAT_API_B2B",
    Scope.corp: "GIGACHAT_API_CORP",
} 
