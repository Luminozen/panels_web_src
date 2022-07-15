import axios from "axios"

// Создать Экземпляр BASE_URL
const BASE_URL = axios.create(
    {
      baseURL: 'http://127.0.0.1:8000/api/',
      headers: {
        contentType: "application/json"
      }
    }
  )
export {BASE_URL}