ninja error `ninja: error: loading 'build.ninja': The system cannot find the file specified`

no se encuentra el archivo `build.ninja`, 

instala manualmente `cmake` y `ninja`
```bash
choco install ninja
choco install cmake
```

Ejecutar 
```bash
cd android
cmake -B build -G Ninja
```

si esto genera un error `CMakeLists.txt`,  en `node_modules/react-native-screens/android/`

entonces el error se debe a que `react-native-screens` esta corrupto, entonces la solución es 
```bash
npm uninstall react-native-screens
npm install react-native-screens
cd android
./gradlew clean
cd ..
npx react-native run-android
```


## refactoring

### Buttons

- `BackButton`
-  `AuthInputFields` (Buttons)
-  `Profile` (BackButtonBar)

### Input field 
- InputField reorganizar bien el codigo, separa logica, ui

### AuthInputFields
migrate `TextInput` to custom `InputField`


|                              |                              |                                                                                                |                                |
| ---------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------ |
| **Computer Science Student** | **Full Stack Web Developer** | **Enthusiastic in Data Science (DS), Artificial Intelligence (AI), and Machine Learning (ML)** | **Always learning new things** |
$(a+b)*(b+c)$
