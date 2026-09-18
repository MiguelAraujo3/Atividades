//Formas de se criar objetos e métodos
const stutent = {
  matriucla: 12312312312,
  name: "Nome Lindo",
  email: "nomelindo@ifpb.com",
  active: false,
  started: 2024,
  getSummary() {
    return `${this.name} (${this.email})`
  },
  situation() {
    if (this.active){
      return `${this.name} está Ativo`
    }
    return `${this.name} está Inativo`
  }
}
const server = new Object();
server.ip = "192.168.0.1";
server.port = 8080;

console.log(stutent.situation())