const base = {
    get() {
        return {
            url : "http://localhost:8080/django6i9a9/",
            name: "django6i9a9",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "学生考勤管理系统"
        } 
    }
}
export default base
