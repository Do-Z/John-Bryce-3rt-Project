// write url from virtual room
// class ProductionConfig {
//     public readonly loginUrl = "http://localhost:8000/api/login";
//     public readonly logoutUrl = "http://localhost:8000/api/logout";
//     public readonly statsUrl = "http://localhost:8000/api/stats";
//     public readonly totalUsersUrl = "http://localhost:8000/api/totalusers";
//     public readonly totalLikesUrl = "http://localhost:8000/api/totallikes";
//     public readonly likesPerCountryUrl = "http://localhost:8000/api/likespercountry";
// }

class DevelopmentConfig {
	public readonly loginUrl = "http://127.0.0.1:8000/api/login";
    public readonly logoutUrl = "http://127.0.0.1:8000/api/logout";
    public readonly statsUrl = "http://127.0.0.1:8000/api/stats";
    public readonly totalUsersUrl = "http://127.0.0.1:8000/api/totalusers";
    public readonly totalLikesUrl = "http://127.0.0.1:8000/api/totallikes";
    public readonly likesPerCountryUrl = "http://127.0.0.1:8000/api/likespercountry";
}

//export const appConfig = new ProductionConfig();
export const appConfig = new DevelopmentConfig();
