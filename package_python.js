





const { exec } = require("child_process");


const command = "conda activate quizlet_app && pyinstaller -w --onefile --add-data web_app/templates;templates --add-data web_app/static;static --distpath dist-python web_app/run_app.py && conda deactivate";


exec(command, (error, stdout, stderr) => {
    if (error) {
        console.log(`error: ${error.message}`);
        return;
    }
    if (stderr) {
        console.log(`stderr: ${stderr}`);
        return;
    }
    console.log(`stdout: ${stdout}`);
});
