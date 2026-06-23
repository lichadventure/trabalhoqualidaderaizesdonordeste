from locust import HttpUser, task, between

class ClienteFranquia(HttpUser):
    # tempo de 1 a 2 s
    wait_time = between(1, 2)

    @task
    def fazer_pedido(self):
        headers = {'Content-Type': 'application/json'}
        
        # O 'catch_response=True' avisa que nos vamos falar o que é erro ou acerto
        with self.client.post("/simular_compra", json={}, headers=headers, catch_response=True) as response:
            
            # Se responder 200, consideramos como ACERTO
            if response.status_code == 200:
                response.success()
                
            # Se responder 400 Estoque Esgotado, consideramos como o ERRO
            elif response.status_code == 400:
                response.failure("Produto esgotado (Erro controlado)")
                
            # Qualquer outra coisa como erro 500
            else:
                response.failure(f"Erro no servidor: {response.status_code}")