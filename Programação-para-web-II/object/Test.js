//Formas de se criar objetos e métodos
const stutent = {
  matricula: 12312312312,
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
const arrayLike = {
  0: 'teste',
  1: 'novo',
  length: 2
}
const server = new Object();
server.ip = "192.168.0.1";
server.port = 8080;
console.log(stutent.matricula)
console.log(stutent.situation())
console.log(typeof[..."teste"]) 
//console.log([...arrayLike]) ERRO, não é "interagível"

const config = {
  thema: "dark",
  fontSize: 12,
  showConfig(){
      console.log(`Tema: ${this.thema}`)
      console.log(`Tamanho da fonte: ${this.fontSize}`)
    }
}

console.log(Object.entries(config))
console.log(Object.values(config))
console.log(Object.keys(config))
config.showConfig()