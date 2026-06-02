from app import app, db, Usuario
from werkzeug.security import generate_password_hash

funcionarios = [
    {"nome": "Michael Scott", "email": "mscott@dunder.com", "senha": "123", "cargo": "Gerente Regional", "departamento": "Gerência", "ramal": "101", "nivel": 2},
    {"nome": "Pam Beesly", "email": "pbeesly@dunder.com", "senha": "123", "cargo": "Admin. de Escritório", "departamento": "Administração", "ramal": "100", "nivel": 3},
    {"nome": "Dwight Schrute", "email": "dschrute@dunder.com", "senha": "123", "cargo": "Vendedor / Ass. Gerente", "departamento": "Vendas", "ramal": "201", "nivel": 1},
    {"nome": "Jim Halpert", "email": "jhalpert@dunder.com", "senha": "123", "cargo": "Vendedor", "departamento": "Vendas", "ramal": "202", "nivel": 1},
    {"nome": "Toby Flenderson", "email": "tflenderson@dunder.com", "senha": "123", "cargo": "Representante de RH", "departamento": "Recursos Humanos", "ramal": "102", "nivel": 3},
    {"nome": "Angela Martin", "email": "amartin@dunder.com", "senha": "123", "cargo": "Contadora Chefe", "departamento": "Contabilidade", "ramal": "300", "nivel": 1},
    {"nome": "Kevin Malone", "email": "kmalone@dunder.com", "senha": "123", "cargo": "Contador", "departamento": "Contabilidade", "ramal": "301", "nivel": 1},
    {"nome": "Oscar Martinez", "email": "omartinez@dunder.com", "senha": "123", "cargo": "Contador", "departamento": "Contabilidade", "ramal": "302", "nivel": 1},
    {"nome": "Stanley Hudson", "email": "shudson@dunder.com", "senha": "123", "cargo": "Vendedor", "departamento": "Vendas", "ramal": "204", "nivel": 1},
    {"nome": "Phyllis Vance", "email": "pvance@dunder.com", "senha": "123", "cargo": "Vendedora", "departamento": "Vendas", "ramal": "205", "nivel": 1},
    {"nome": "Andy Bernard", "email": "abernard@dunder.com", "senha": "123", "cargo": "Vendedor", "departamento": "Vendas", "ramal": "203", "nivel": 1},
    {"nome": "Creed Bratton", "email": "cbratton@dunder.com", "senha": "123", "cargo": "Garantia de Qualidade", "departamento": "Qualidade", "ramal": "403", "nivel": 1},
    {"nome": "Meredith Palmer", "email": "mpalmer@dunder.com", "senha": "123", "cargo": "Relações com Fornecedores", "departamento": "Suprimentos", "ramal": "402", "nivel": 1},
    {"nome": "Kelly Kapoor", "email": "kkapoor@dunder.com", "senha": "123", "cargo": "Atendimento ao Cliente", "departamento": "Suporte", "ramal": "401", "nivel": 1},
    {"nome": "Ryan Howard", "email": "rhoward@dunder.com", "senha": "123", "cargo": "Temporário", "departamento": "Diversos", "ramal": "109", "nivel": 1},
    {"nome": "Darryl Philbin", "email": "dphilbin@dunder.com", "senha": "123", "cargo": "Encarregado do Depósito", "departamento": "Logística", "ramal": "501", "nivel": 1},
    {"nome": "Erin Hannon", "email": "ehannon@dunder.com", "senha": "123", "cargo": "Recepcionista", "departamento": "Administração", "ramal": "103", "nivel": 1}
]

with app.app_context():
    db.drop_all()
    db.create_all()

    for f in funcionarios:
        senha_criptografada = generate_password_hash(f["senha"])

        novo_usuario = Usuario(
            nome=f["nome"],
            email=f["email"],
            senha=senha_criptografada, 
            cargo=f["cargo"],
            departamento=f["departamento"],
            ramal=f["ramal"],
            nivel_acesso=f["nivel"]
        )
        db.session.add(novo_usuario)
    
    db.session.commit()
    print("🏢 Dunder Mifflin completa! Todos os 17 funcionários foram cadastrados com sucesso!")