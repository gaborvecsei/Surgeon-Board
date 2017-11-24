package com.gabor.vecsei.accelerometerrecorder;

import android.os.Environment;
import android.util.Log;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

/**
 * Created by Gábor on 11/24/2017
 */

public class RawAccelerometerDataCreator {

    private static SimpleDateFormat TIMESTAMP_FORMAT = new SimpleDateFormat("yyyyMMddHHmmss", Locale.getDefault());
    private static String CSV_HEADER = "elapsed_millis,x,y,z,\n";
    private String userFileName;
    private FileOutputStream fileOutputStream;
    private long startTime;

    public RawAccelerometerDataCreator(String userFileName) {
        this.userFileName = userFileName;
        this.startTime = System.currentTimeMillis();
        String timestamp = TIMESTAMP_FORMAT.format(new Date());
        String fileName = this.userFileName + ".accelerometer_raw_data_" + timestamp + ".csv";

        File sdCard = Environment.getExternalStorageDirectory();
        File dir = new File(sdCard.getAbsolutePath() + "/collected_accelerometer_data");
        Boolean isDirMade = dir.mkdir();
        Log.d("Folder creation", String.valueOf(isDirMade));
        File outputFile = new File(dir, fileName);

        try {
            this.fileOutputStream = new FileOutputStream(outputFile, true);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        try {
            this.fileOutputStream.write(CSV_HEADER.getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String createDataEntry(float x, float y, float z) {
        long endTime = System.currentTimeMillis();
        long elapsedTimeInMillis = endTime - startTime;
        return elapsedTimeInMillis + "," + x + "," + y + "," + z + "," + "\n";
    }

    public void addDataRowToFile(String row) {
        try {
            fileOutputStream.write(row.getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void stopReceivingData() {
        try {
            fileOutputStream.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
