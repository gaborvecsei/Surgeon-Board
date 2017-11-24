package com.gabor.vecsei.accelerometerrecorder;

import android.Manifest;
import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.os.Vibrator;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.Toast;

import com.getwandup.rxsensor.RxSensor;
import com.getwandup.rxsensor.domain.RxSensorEvent;
import com.tbruyelle.rxpermissions.RxPermissions;

import rx.Subscriber;
import rx.functions.Action1;

public class MainActivity extends AppCompatActivity {

    Spinner actionSelectorSpinner;
    Button recordButton;

    private boolean isRecording;
    private RawAccelerometerDataCreator tmpRawData;
    private Subscriber accelerometerSubscriber;
    Vibrator vibrator;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        actionSelectorSpinner = (Spinner) findViewById(R.id.action_selector_spinner);
        recordButton = (Button) findViewById(R.id.record_button);
        vibrator = (Vibrator) getSystemService(Context.VIBRATOR_SERVICE);

        setupSpinner();
        checkPermissions();

        recordButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                recordButtonPressed();
            }
        });
    }

    private void setupSpinner() {
        String[] availableActions = new String[]{"up_arrow", "circle", "horizontal_line", "other"};
        ArrayAdapter<String> actionsAdapter = new ArrayAdapter<>(this, android.R.layout.simple_spinner_dropdown_item, availableActions);
        actionSelectorSpinner.setAdapter(actionsAdapter);

    }

    private void checkPermissions() {
        RxPermissions rxPermissions = new RxPermissions(MainActivity.this);
        rxPermissions
                .request(Manifest.permission.WRITE_EXTERNAL_STORAGE, Manifest.permission.READ_EXTERNAL_STORAGE)
                .subscribe(new Action1<Boolean>() {
                    @Override
                    public void call(Boolean aBoolean) {
                        if (aBoolean) {
                            // Granted
                            Toast.makeText(MainActivity.this, "Permissions granted", Toast.LENGTH_SHORT).show();
                        } else {
                            // Not granted
                            MainActivity.super.finish();
                        }
                    }
                });
    }

    private void recordButtonPressed() {
        if (!isRecording) {
            isRecording = true;
            tmpRawData = new RawAccelerometerDataCreator(actionSelectorSpinner.getSelectedItem().toString());
            startAccelerometerRecording();
            recordButton.setText("Stop Recording");
        } else {
            stopAcceleratorRecording();
            if (tmpRawData != null) {
                tmpRawData.stopReceivingData();
                tmpRawData = null;
            }
            isRecording = false;
            vibrator.vibrate(100);
            vibrator.vibrate(100);
            recordButton.setText("Start Recording");
        }
    }

    private void startAccelerometerRecording() {
        RxSensor rxSensor = new RxSensor(this);
        accelerometerSubscriber = new Subscriber<RxSensorEvent>() {
            @Override
            public void onCompleted() {

            }

            @Override
            public void onError(Throwable e) {

            }

            @Override
            public void onNext(RxSensorEvent sensorEvent) {
                float x = sensorEvent.values[0];
                float y = sensorEvent.values[1];
                float z = sensorEvent.values[2];

                tmpRawData.addDataRowToFile(tmpRawData.createDataEntry(x, y, z));
            }
        };

        rxSensor.observe(Sensor.TYPE_ACCELEROMETER, SensorManager.SENSOR_DELAY_NORMAL)
                .subscribe(accelerometerSubscriber);
    }

    private void stopAcceleratorRecording() {
        if (accelerometerSubscriber != null) {
            accelerometerSubscriber.unsubscribe();
        }
    }

    @Override
    public void finish() {
        if (!isRecording) {
            super.finish();
        }
    }
}
